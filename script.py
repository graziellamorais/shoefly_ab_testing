# Import the necessary libraries
import codecademylib3  # Codecademy-specific library for compatibility
import pandas as pd  # Import pandas for data manipulation and analysis

# Load the dataset into a DataFrame
user_visits = pd.read_csv('page_visits.csv')

# Part 1: Display the first 10 rows of the dataset
print(user_visits.head(10))

# Part 2: Group data by 'utm_source' and count the number of occurrences of 'id' for each source
# This shows how many visits each source generated
click_source = user_visits.groupby('utm_source').id.count().reset_index()

# Part 3: Display the summarized data showing the number of visits by source
print(click_source)

# Part 4: Group data by both 'utm_source' and 'month' and count the number of visits for each combination
click_source_by_month = user_visits.groupby(['utm_source', 'month']).id.count().reset_index()

# Print the grouped data by source and month
print(click_source_by_month)

# Part 5: Create a pivot table to organize the data, with 'month' values as columns,
# 'utm_source' as index, and the count of 'id' as values
click_source_by_month_pivot = click_source_by_month.pivot(
    columns='month',
    index='utm_source',
    values='id').reset_index()

# Part 6: Display the pivot table to see the number of visits per source for each month
print(click_source_by_month_pivot)
