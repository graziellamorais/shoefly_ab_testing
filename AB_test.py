import codecademylib3
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

print(ad_clicks.head())

# Which ad platform is getting the most views?
views_count = ad_clicks.groupby('utm_source').user_id.count().reset_index()
print(views_count)

# Create a new column called is_click, which is True if ad_click_timestamp is not null and False otherwise.
ad_clicks['is_click'] = ~ad_clicks\
   .ad_click_timestamp.isnull()
print(ad_clicks)

'''
We want to know the percent of people who clicked on ads from each utm_source.

Start by grouping by utm_source and is_click and counting the number of user_id's in each of those groups. Save your answer to the variable clicks_by_source.
'''
clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()

# Pivoting the table so that the columns are is_click, the index is utm_source and the values are user_id
clicks_pivot = clicks_by_source.pivot(index='utm_source', columns = 'is_click', values='user_id').reset_index()

'''
Create a new column in clicks_pivot called percent_clicked which is equal to the percent of users who clicked on the ad from each utm_source.

Was there a difference in click rates for each source?
'''
clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])

'''
clicks_pivot[True] is the number of people who clicked (because is_click was True for those users)

clicks_pivot[False] is the number of people who did not click (because is_click was False for those users)

So, the percent of people who clicked would be (Total Who Clicked) / (Total Who Clicked + Total Who Did Not Click)
'''

'''

The column experimental_group tells us whether the user was shown Ad A or Ad B.

Were approximately the same number of people shown both ads?
'''
# Group by 'experimental_group' and 'is_click' and count 'user_id'
most_clicked_ad = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()

# Create a pivot table
most_clicked_ad_pivot = most_clicked_ad.pivot(index='experimental_group', columns='is_click', values='user_id').reset_index()

# Fill any missing values with 0 (in case there are no clicks or no non-clicks)
most_clicked_ad_pivot = most_clicked_ad_pivot.fillna(0)

# Calculate the percentage of users who clicked on the ad
most_clicked_ad_pivot['percent_clicked'] = (most_clicked_ad_pivot[True] / (most_clicked_ad_pivot[True] + most_clicked_ad_pivot[False]) * 100).round(2)

print(most_clicked_ad_pivot)

'''
The Product Manager for the A/B test thinks that the clicks might have changed by day of the week.

Start by creating two DataFrames: a_clicks and b_clicks, which contain only the results for A group and B group, respectively.
'''
# Filter for group A
a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']

# Group by 'day' and 'is_click', then count 'user_id'
clicks_by_day_A = a_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()

# Create a pivot table
clicks_by_day_A_pivot = clicks_by_day_A.pivot(index='day', columns='is_click', values='user_id').fillna(0).reset_index()

# Calculate the percentage of clicks per day (rounded to 2 decimal points)
clicks_by_day_A_pivot['percent_clicked'] = (clicks_by_day_A_pivot[True] / 
                                            (clicks_by_day_A_pivot[True] + clicks_by_day_A_pivot[False]) * 100).round(2)

print(clicks_by_day_A_pivot)

# Filter for group B
a_clicks = ad_clicks[ad_clicks.experimental_group == 'B']

# Group by 'day' and 'is_click', then count 'user_id'
clicks_by_day_B = a_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()

# Create a pivot table
clicks_by_day_B_pivot = clicks_by_day_B.pivot(index='day', columns='is_click', values='user_id').fillna(0).reset_index()

# Calculate the percentage of clicks per day (rounded to 2 decimal points)
clicks_by_day_B_pivot['percent_clicked'] = (clicks_by_day_B_pivot[True] / 
                                            (clicks_by_day_B_pivot[True] + clicks_by_day_B_pivot[False]) * 100).round(2)

print(clicks_by_day_B_pivot)

'''
Compare the results for A and B. What happened over the course of the week?

Do you recommend that your company use Ad A or Ad B?
'''
comparison = clicks_by_day_A_pivot.merge(clicks_by_day_B_pivot, on='day', suffixes=('_A', '_B'))
print(comparison)

'''
Analysis:
Ad A consistently outperformed Ad B in terms of click percentage on most days:

Ad A had a higher click rate than Ad B on Monday, Wednesday, Thursday, Friday, and Sunday.
Ad B only performed better on Tuesday and Saturday — but the differences weren't very large.
Highest engagement for Ad A:

Thursday (40.52%) and Friday (39.84%) had the highest click rates for Ad A.
Ad A maintained a relatively stable click rate, hovering around 38%...40% on most days.
Lowest engagement for Ad B:

Ad B performed worst on Thursday (25%) and Wednesday (28.23%).
It's highest performance was on Tuesday (37.82%) and Saturday (35.59%), but still not consistently better than Ad A.
'''
