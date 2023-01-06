import pandas as pd

STEPS = [0, 20, 40, 80]
counts = [0, 0, 0, 0, 0, 0, 0, 0]


def calculate_row_range(row_, level):
    step = STEPS[level]
    counts[level] += 1
    if counts[level] >= step:
        counts[level] = 0

    return f"{row_ - counts[level]}-{row_ - counts[level] + step}"


if __name__ == "__main__":
    adult_df = pd.read_csv("input-data/adult-dataset.csv")
    hours = adult_df["hours-per-week"].unique()

    rows = range(1, 100)
    age_df = pd.DataFrame(columns=[f"level-{i}" for i, step in enumerate(STEPS)])

    for row in rows:
        level_1 = calculate_row_range(row, 1)
        level_2 = calculate_row_range(row, 2)
        level_3 = calculate_row_range(row, 3)

        df = pd.DataFrame(
            [
                {
                    "level-0": str(row),
                    "level-1": level_1,
                    "level-2": level_2,
                    "level-3": level_3,
                    "level-7": "any",
                }
            ]
        )
        age_df = pd.concat([age_df, df], ignore_index=True)

    filename = "taxonomy-trees/scenario-a/coarse/scenario-a-coarse-tax-hours-per-week.csv"
    print(f"Filename: {filename}")
    print("generate tree? ('y' or 'n')")

    if "y" in input():
        age_df.to_csv(filename, index=False)

    breakpoint()
