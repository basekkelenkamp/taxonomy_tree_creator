import pandas as pd

STEPS = [0, 1, 2, 3, 5, 7, 9]
counts = [0] * len(STEPS)


def calculate_row_range(row_, level):
    step = STEPS[level]
    counts[level] += 1
    if counts[level] > step:
        counts[level] = 0

    return f"{row_ - counts[level]}-{row_ - counts[level] + step}"


if __name__ == "__main__":
    adult_df = pd.read_csv("adult-dataset.csv")
    edu = adult_df["education-num"].unique()

    rows = range(min(edu), max(edu)+1)
    edu_df = pd.DataFrame(columns=[f"level-{i}" for i, step in enumerate(STEPS)])

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
        edu_df = pd.concat([edu_df, df], ignore_index=True)

    breakpoint()
    edu_df.to_csv("education_num_taxonimy_tree.csv", index=False)

    breakpoint()
