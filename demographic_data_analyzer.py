import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? 
    race_count = df["race"].value_counts()

    # What is the average age of men?
    average_age_men = df.groupby("sex")["age"].mean()
    # average_age_men = average_age_men0.iloc[0,0]


    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = ((df["education"]).value_counts()["Bachelors"] / df["education"].value_counts().sum())*100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education0 = df[df["education"].isin(["Bachelors", "Masters", "Doctorate"])]
    higher_education = (higher_education0["education"].value_counts()).sum()
    lower_education =  (df["education"].value_counts()).sum() - higher_education

    # percentage with salary >50K
    higher_education_rich = (higher_education0["salary"].value_counts()[">50K"].sum()  / higher_education) * 100
    lower_education_rich = (higher_education0["salary"].value_counts()["<=50K"].sum()  / lower_education) * 100

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df["salary"] == ">50K") & (df["native-country"] == "India")]["occupation"].value_counts().idxmax()


    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'top_IN_occupation': top_IN_occupation
    }
calculate_demographic_data()
df = pd.read_csv("adult.data.csv")

