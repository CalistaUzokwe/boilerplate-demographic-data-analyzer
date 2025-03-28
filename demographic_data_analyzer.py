import pandas as pd

# Load the dataset
df = pd.read_csv("adult.data.csv", header=None)

# Display the first few rows
print(df.head())

def calculate_demographic_data(print_data=True):
# use the loaded dataset
  global df

# How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
race_count = race_count = df[8].value_counts()

# What is the average age of men?
average_age_men = average_age_men = df[df[9] == "Male"][0].mean()

# What is the percentage of people who have a Bachelor's degree?
percentage_bachelors = percentage_bachelors = (df[df[3] == "Bachelors"].shape[0] / df.shape[0]) * 100

# What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
# What percentage of people without advanced education make more than 50K?

# with and without `Bachelors`, `Masters`, or `Doctorate`
higher_education = higher_education = df[df[3].isin(["Bachelors", "Masters", "Doctorate"])]
higher_education_rich = (higher_education[higher_education[14] == ">50K"].shape[0] / higher_education.shape[0]) * 100

lower_education =  lower_education = df[~df[3].isin(["Bachelors", "Masters", "Doctorate"])]
lower_education_rich = (lower_education[lower_education[14] == ">50K"].shape[0] / lower_education.shape[0]) * 100

# percentage with salary >50K
higher_education_rich = higher_education_rich = (higher_education[higher_education[14] == ">50K"].shape[0] / higher_education.shape[0]) * 100

lower_education_rich = lower_education_rich = (lower_education[lower_education[14] == ">50K"].shape[0] / lower_education.shape[0]) * 100


# What is the minimum number of hours a person works per week (hours-per-week feature)?
min_work_hours = min_work_hours = df[12].min()

# What percentage of the people who work the minimum number of hours per week have a salary of >50K?
num_min_workers = num_min_workers = df[df[12] == min_work_hours]
rich_percentage = (num_min_workers[num_min_workers[14] == ">50K"].shape[0] / num_min_workers.shape[0]) * 100

rich_percentage = rich_percentage = (num_min_workers[num_min_workers[14] == ">50K"].shape[0] / num_min_workers.shape[0]) * 100


# What country has the highest percentage of people that earn >50K?
country_salary_counts = df[df["salary"] == ">50K"]["native-country"].value_counts()

highest_earning_country_percentage = highest_earning_country_percentage = country_salary_counts[">50K"].max() * 100

# Identify the most popular occupation for those who earn >50K in India.
top_IN_occupation = top_IN_occupation = df[(df[13] == "India") & (df[14] == ">50K")][6].value_counts().idxmax()


# DO NOT MODIFY BELOW THIS LINE

if print_data:
    print("Number of each race:\n", race_count) 
    print("Average age of men:", average_age_men)
    print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
    print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
    print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
    print(f"Min work time: {min_work_hours} hours/week")
    print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
    print("Country with highest percentage of rich:", highest_earning_country)
    print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
    print("Top occupations in India:", top_IN_occupation)
    def demographic_data_analyzer():
    # Your calculations here
    
        return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

