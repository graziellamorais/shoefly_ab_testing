import pandas as pd

# Load the dataset
ad_clicks = pd.read_csv('ad_clicks.csv')

# Display the first few rows of the dataset
print(ad_clicks.head())

# Function to calculate the number of views per ad platform
def calculate_views(ad_clicks):
    views_count = ad_clicks.groupby('utm_source').user_id.count().reset_index()
    return views_count

# Display the result of the views calculation
views_count = calculate_views(ad_clicks)
print(views_count)

# Function to create a new column `is_click` that checks if an ad click occurred
def add_is_click_column(ad_clicks):
    ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()
    return ad_clicks

# Add the `is_click` column and display the result
ad_clicks = add_is_click_column(ad_clicks)
print(ad_clicks)

# Function to calculate the percent of users who clicked the ad for each utm_source
def calculate_click_percentage(ad_clicks):
    # Group by `utm_source` and `is_click`, then count the number of user_id's in each group
    clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()

    # Pivot the table to get the clicks and non-clicks for each `utm_source`
    clicks_pivot = clicks_by_source.pivot(index='utm_source', columns='is_click', values='user_id').reset_index()

    # Calculate the percentage of users who clicked
    clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])

    return clicks_pivot

# Display the click percentage result
clicks_pivot = calculate_click_percentage(ad_clicks)
print(clicks_pivot)

# Function to calculate the number of clicks and non-clicks for each experimental group
def calculate_clicks_by_experimental_group(ad_clicks):
    # Group by 'experimental_group' and 'is_click' to count user_id's
    most_clicked_ad = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()

    # Pivot the table to show clicks and non-clicks for each group
    most_clicked_ad_pivot = most_clicked_ad.pivot(index='experimental_group', columns='is_click', values='user_id').reset_index()

    # Fill any missing values with 0
    most_clicked_ad_pivot = most_clicked_ad_pivot.fillna(0)

    # Calculate the percentage of users who clicked on each ad
    most_clicked_ad_pivot['percent_clicked'] = (most_clicked_ad_pivot[True] / 
                                               (most_clicked_ad_pivot[True] + most_clicked_ad_pivot[False]) * 100).round(2)

    return most_clicked_ad_pivot

# Display the clicks by experimental group result
most_clicked_ad_pivot = calculate_clicks_by_experimental_group(ad_clicks)
print(most_clicked_ad_pivot)

# Function to calculate the click percentage by day for a specific experimental group (A or B)
def calculate_clicks_by_day(ad_clicks, group):
    # Filter the data for the experimental group (A or B)
    group_clicks = ad_clicks[ad_clicks.experimental_group == group]

    # Group by 'day' and 'is_click', then count the number of user_id's
    clicks_by_day = group_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()

    # Pivot the table to get the clicks and non-clicks for each day
    clicks_by_day_pivot = clicks_by_day.pivot(index='day', columns='is_click', values='user_id').fillna(0).reset_index()

    # Calculate the percentage of clicks per day
    clicks_by_day_pivot['percent_clicked'] = (clicks_by_day_pivot[True] / 
                                              (clicks_by_day_pivot[True] + clicks_by_day_pivot[False]) * 100).round(2)

    return clicks_by_day_pivot

# Calculate and display the click percentage by day for Ad A
clicks_by_day_A_pivot = calculate_clicks_by_day(ad_clicks, 'A')
print(clicks_by_day_A_pivot)

# Calculate and display the click percentage by day for Ad B
clicks_by_day_B_pivot = calculate_clicks_by_day(ad_clicks, 'B')
print(clicks_by_day_B_pivot)

# Function to compare the results between experimental groups A and B
def compare_ads_by_day(ad_clicks):
    # Get the clicks by day for both Ad A and Ad B
    clicks_by_day_A_pivot = calculate_clicks_by_day(ad_clicks, 'A')
    clicks_by_day_B_pivot = calculate_clicks_by_day(ad_clicks, 'B')

    # Merge the two dataframes on 'day' to compare the results
    comparison = clicks_by_day_A_pivot.merge(clicks_by_day_B_pivot, on='day', suffixes=('_A', '_B'))

    return comparison

# Display the comparison results between Ad A and Ad B
comparison = compare_ads_by_day(ad_clicks)
print(comparison)

# Analysis:
# - Ad A consistently outperformed Ad B in terms of click percentage on most days.
# - Ad A had higher click rates on Monday, Wednesday, Thursday, Friday, and Sunday.
# - Ad B only performed better on Tuesday and Saturday, but the differences weren't significant.
# - Ad A maintained a relatively stable click rate, with Thursday and Friday having the highest click rates (around 40%).
# - Ad B had the lowest engagement on Thursday (25%) and Wednesday (28.23%), with its highest performance on Tuesday (37.82%) and Saturday (35.59%).
