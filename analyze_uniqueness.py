import pandas as pd

quasi_a = [
    "age",
    "work-class",
    "education",
    "education-num",
    "marital-status",
    "occupation",
    "relationship",
    "sex",
    "hours-per-week",
    "native-country",
    "income",
]


if __name__ == "__main__":

    scenario = "a"
    original_df = pd.read_csv(
        f"output-data/transformed-dataset-3.4/scenario-{scenario}-detailed/scenario_{scenario}_detailed_k10.csv"
    )
    quasi_b = original_df.columns.values.tolist()

    # Group the records by quasi columns
    grouped_data = original_df.groupby(quasi_a)

    # Count the number of records in each group
    group_size = grouped_data.size()

    # Calculate the percentage of unique records
    summed = (group_size == 1).sum()
    unique_records = summed / len(original_df) * 100
    print("Percentage of unique records:", unique_records, "%")
    print("Amount of records:", summed)
