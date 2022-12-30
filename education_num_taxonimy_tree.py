import pandas as pd

STEPS = [0, 5, 10]
counts = [0] * len(STEPS)


def calculate_row_range(row_, level):
    step = STEPS[level]
    counts[level] += 1
    if counts[level] >= step:
        counts[level] = 0

    return f"{row_ - counts[level]}-{row_ - counts[level] + step}"


if __name__ == "__main__":
    adult_df = pd.read_csv("input-data/adult-dataset.csv")
    edu = adult_df["education-num"].unique()
    rows = range(min(edu), max(edu) + 1)

    edu_df = pd.DataFrame(columns=[f"level-{i}" for i, step in enumerate(STEPS)])

    for row in rows:
        level_1 = calculate_row_range(row, 1)
        level_2 = calculate_row_range(row, 2)

        df = pd.DataFrame(
            [
                {
                    "level-0": str(row),
                    "level-1": level_1,
                    "level-2": level_2,
                    "level-3": "any",
                }
            ]
        )
        edu_df = pd.concat([edu_df, df], ignore_index=True)

    filename = "output-data/scenario-b/coarse/scenario-b-coarse-education-num.csv"
    print(f"Filename: {filename}")
    print("generate tree? ('y' or 'n')")

    if "y" in input():
        edu_df.to_csv(filename, index=False)

    breakpoint()
