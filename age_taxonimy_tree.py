import pandas as pd

STEPS = [0, 1, 5, 10, 20, 40, 80]
counts = [0, 0, 0, 0, 0, 0, 0, 0]


def calculate_row_range(row_, level):
    step = STEPS[level]
    counts[level] += 1
    if counts[level] >= step:
        counts[level] = 0

    return f"{row_ - counts[level]}-{row_ - counts[level] + step}"


if __name__ == "__main__":
    # adult_df = pd.read_csv("input/adult-dataset.csv")
    # columns = adult_df.columns.tolist()
    # print(adult_df['age'].unique())

    rows = range(1, 100)
    age_df = pd.DataFrame(columns=[f"level-{i}" for i, step in enumerate(STEPS)])

    for row in rows:
        level_1 = calculate_row_range(row, 1)
        level_2 = calculate_row_range(row, 2)
        level_3 = calculate_row_range(row, 3)
        level_4 = calculate_row_range(row, 4)
        level_5 = calculate_row_range(row, 5)
        level_6 = calculate_row_range(row, 6)

        df = pd.DataFrame(
            [
                {
                    "level-0": str(row),
                    "level-1": level_1,
                    "level-2": level_2,
                    "level-3": level_3,
                    "level-4": level_4,
                    "level-5": level_5,
                    "level-6": level_6,
                    "level-7": "any",
                }
            ]
        )
        age_df = pd.concat([age_df, df], ignore_index=True)

    print("generate tree? ('y' or 'n')")
    if 'y' in input():
        age_df.to_csv(f"output-data/scenario-a-detailed-tax-age.csv", index=False)

    breakpoint()
