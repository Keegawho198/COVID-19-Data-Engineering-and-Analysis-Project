import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import seaborn as sns
from datetime import datetime

# Define the path for the resources directory 
path = Path("Resources/")

# Load CSV files into pandas DataFrames
countries_dataset = pd.read_csv("Resources/countries.csv")
covid_cases_dataset = pd.read_csv("Resources/WHO COVID-19 cases.csv")

# Rename columns in countries dataset for clarity
countries_dataset = countries_dataset.rename(columns={'country':'Country_code', 'name':'Country'})
countries_dataset.head()

# Merge datasets on common column 'Country_code'
complete_dataset = pd.merge(covid_cases_dataset, countries_dataset, on="Country_code")
complete_dataset.head()

# Drop unnecessary column
complete_dataset = complete_dataset.drop(columns=["Country_y"])
complete_dataset.head()

# Rename columns for consistency and clarity
complete_dataset = complete_dataset.rename(columns={
    "Date_reported":"Date",
    "Country_code":"Country Code",
    "Country_x":"Country",
    "WHO_region":"WHO Region",
    "New_cases":"New Cases",
    "Cumulative_cases":"Cumulative Cases",
    "New_deaths":"New Deaths",
    "Cumulative_deaths":"Cumulative Deaths",
    "latitude":"Latitude",
    "longitude":"Longitude"
})
complete_dataset.head()

#identify empty and Nan rows
complete_dataset.count()

# Remove duplicate rows and drop rows with any missing values
complete_dataset = complete_dataset.drop_duplicates().dropna(how='any')
complete_dataset.head()

# Check if NaN and zero value rows and columns were removed
complete_dataset.count()

#check the datatypes
complete_dataset.dtypes

# Change 'Date' column to datetime type
complete_dataset['Date'] = pd.to_datetime(complete_dataset['Date'])
#check if date datatypes changed
complete_dataset.dtypes

# Aggregation: Group by country with additional statistics
country_group_data = complete_dataset.groupby('Country').agg({
    'New Cases': ['sum', 'mean', 'std'],
    'New Deaths': ['sum', 'mean', 'std']
})
country_group_data.head()

# Use aggregation to find the max, min cases and deaths globally
country_stats = complete_dataset.groupby('Country').agg({
    'Cumulative Cases': 'max',
    'Cumulative Deaths': 'max'
}).reset_index()

# Find countries with maximum and minimum cases and deaths
max_cases_country = country_stats.loc[country_stats['Cumulative Cases'].idxmax()]
min_cases_country = country_stats.loc[country_stats['Cumulative Cases'].idxmin()]
max_deaths_country = country_stats.loc[country_stats['Cumulative Deaths'].idxmax()]
min_deaths_country = country_stats.loc[country_stats['Cumulative Deaths'].idxmin()]

# Display results
print("Country with Maximum Cases:", max_cases_country)
print("Country with Minimum Cases:", min_cases_country)
print("Country with Maximum Deaths:", max_deaths_country)
print("Country with Minimum Deaths:", min_deaths_country)

# Filter data for Australia
australia_data = complete_dataset[complete_dataset['Country'] == 'Australia']
print(australia_data.head())

# Calculate average new cases in Australia
average_cases = australia_data['New Cases'].mean()
print(f"Average COVID-19 cases in Australia: {average_cases:.2f}")

# Find the day with maximum and minimum cases and deaths in Australia
max_cases_day = australia_data.loc[australia_data['New Cases'].idxmax()]
min_cases_day = australia_data.loc[australia_data['New Cases'].idxmin()]
max_deaths_day = australia_data.loc[australia_data['New Deaths'].idxmax()]
min_deaths_day = australia_data.loc[australia_data['New Deaths'].idxmin()]

# Display results
print(f"Maximum cases: {max_cases_day['New Cases']} on {max_cases_day['Date'].date()}")
print(f"Minimum cases: {min_cases_day['New Cases']} on {min_cases_day['Date'].date()}")
print(f"Maximum deaths: {max_deaths_day['New Deaths']} on {max_deaths_day['Date'].date()}")
print(f"Minimum deaths: {min_deaths_day['New Deaths']} on {min_deaths_day['Date'].date()}")

# Summarize data for Australia using pivot_table()
pivot_summary = australia_data.pivot_table(
    index='Date', values=['New Cases', 'New Deaths'], aggfunc='sum'
).astype(int)
pivot_summary

# Visualize pivot table summary
pivot_summary.plot(kind='line', figsize=(10, 6), title='New Cases and Deaths Over Time in Australia')
plt.xlabel('Date')
plt.ylabel('Count')
plt.legend(title='Metrics')
plt.show()

# Display ETL results before exporting data
complete_dataset.head()

# Export complete dataset to CSV
complete_dataset.to_csv("Resources/complete_dataset.csv", index=False)