import pandas as pd

# Load the dataset
df = pd.read_csv("adult.data.csv", header=None)

# Define column names to avoid confusion
df.columns = ["age", "workclass", "fnlwgt", "education", "education-num",
              "marital-status", "occupation", "relationship", "race",
              "sex", "capital-gain", "capital-loss", "hours-per-week",
              "native-country", "salary"]

# Display the first few rows
print(df.head())

def calculate_demographic_data(print_data=True):
    # Race count
    race_count = df["race"].value_counts()

    # Average age of men
    average_age_men = df[df["sex"] == "Male"]["age"].mean()

    # Percentage of people with a Bachelor's degree
    percentage_bachelors = (df[df["education"] == "Bachelors"].shape[0] / df.shape[0]) * 100

    # Higher and lower education categories
    higher_education = df[df["education"].isin(["Bachelors", "Masters", "Doctorate"])]
    lower_education = df[~df["education"].isin(["Bachelors", "Masters", "Doctorate"])]

    # Percentage of people with advanced education earning >50K
    higher_education_rich = (higher_education[higher_education["salary"] == ">50K"].shape[0] / higher_education.shape[0]) * 100

    # Percentage of people without advanced education earning >50K
    lower_education_rich = (lower_education[lower_education["salary"] == ">50K"].shape[0] / lower_education.shape[0]) * 100

    # Minimum work hours per week
    min_work_hours = df["hours-per-week"].min()

    # Percentage of people working min hours earning >50K
    num_min_workers = df[df["hours-per-week"] == min_work_hours]
    rich_percentage = (num_min_workers[num_min_workers["salary"] == ">50K"].shape[0] / num_min_workers.shape[0]) * 100

    # Highest earning country (fix: define country_salary_counts)
    country_salary_counts = df.groupby("native-country")["salary"].value_counts(normalize=True).unstack()
    highest_earning_country = country_salary_counts[">50K"].idxmax()
    highest_earning_country_percentage = country_salary_counts[">50K"].max() * 100

    # Most common occupation in India for those earning >50K
    top_IN_occupation = df[(df["native-country"] == "India") & (df["salary"] == ">50K")]["occupation"].value_counts().idxmax()

    # Print results if print_data is True
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
        print("Top occupation in India:", top_IN_occupation)

    # Return results as dictionary
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

# Call function
calculate_demographic_data(print_data=True)


