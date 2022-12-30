import pandas as pd

STEPS = [0, 10, 20, 40]
counts = [0, 0, 0, 0, 0, 0, 0, 0]


def calculate_row_range(row_, level):
    step = STEPS[level]
    counts[level] += 1
    if counts[level] >= step:
        counts[level] = 0

    return f"{row_ - counts[level]}-{row_ - counts[level] + step}"


if __name__ == "__main__":
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
                    "level-4": "any",
                }
            ]
        )
        age_df = pd.concat([age_df, df], ignore_index=True)

    filename = "output-data/scenario-a-coarse-tax-age.csv"
    print(f"Filename: {filename}")
    print("generate tree? ('y' or 'n')")

    if 'y' in input():
        age_df.to_csv(filename, index=False)

    breakpoint()
