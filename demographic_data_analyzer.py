import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # 1. How many of each race are represented?
    race_count = df["race"].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df["sex"] == "Male"]["age"].mean(), 1)

    # 3. Percentage with Bachelors
    percentage_bachelors = round(
        (df[df["education"] == "Bachelors"].shape[0] / df.shape[0]) * 100, 1
    )

    # 4. Percentage with advanced education earning >50K
    higher_education = df[df["education"].isin(["Bachelors", "Masters", "Doctorate"])]

    lower_education = df[~df["education"].isin(["Bachelors", "Masters", "Doctorate"])]

    higher_education_rich = round(
        (higher_education[higher_education["salary"] == ">50K"].shape[0] / higher_education.shape[0]) * 100,
        1
    )

    # 5. Percentage without advanced education earning >50K
    lower_education_rich = round(
        (lower_education[lower_education["salary"] == ">50K"].shape[0] / lower_education.shape[0]) * 100,
        1
    )

    # 6. Minimum work hours per week
    min_work_hours = df["hours-per-week"].min()

    # 7. Percentage of people who work minimum hours and earn >50K
    num_min_workers = df[df["hours-per-week"] == min_work_hours]

    rich_percentage = round(
        (num_min_workers[num_min_workers["salary"] == ">50K"].shape[0] / num_min_workers.shape[0]) * 100,
        1
    )

    # 8. Country with highest percentage of people earning >50K
    country_salary_counts = df[df["salary"] == ">50K"]["native-country"].value_counts()
    country_total_counts = df["native-country"].value_counts()

    country_rich_percentage = (country_salary_counts / country_total_counts) * 100

    highest_earning_country = country_rich_percentage.idxmax()
    highest_earning_country_percentage = round(country_rich_percentage.max(), 1)

    # 9. Most popular occupation for people earning >50K in India
    top_IN_occupation = (
        df[(df["native-country"] == "India") & (df["salary"] == ">50K")]
        ["occupation"]
        .value_counts()
        .idxmax()
    )

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

    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation,
    }
