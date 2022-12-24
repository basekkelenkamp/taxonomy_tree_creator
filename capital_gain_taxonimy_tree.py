import pandas as pd

STEPS = [0, 100, 500, 1000, 2500, 7500]
counts = [0] * len(STEPS)


def calculate_row_range(row_, level):
    step = STEPS[level]
    counts[level] += 1
    if counts[level] > step:
        counts[level] = 0

    return f"{row_ - counts[level]}-{row_ - counts[level] + step}"


if __name__ == "__main__":
    adult_df = pd.read_csv("adult-dataset.csv")
    cap = adult_df["capitical-gain"].unique()

    rows = range(min(cap), max(cap)+1, 500)
    cap_df = pd.DataFrame(columns=[f"level-{i}" for i, step in enumerate(STEPS)])

    for row in rows:
        level_1 = calculate_row_range(row, 1)
        level_2 = calculate_row_range(row, 2)
        level_3 = calculate_row_range(row, 3)
        level_4 = calculate_row_range(row, 4)
        level_5 = calculate_row_range(row, 5)

        df = pd.DataFrame(
            [
                {
                    "level-0": str(row),
                    "level-1": level_1,
                    "level-2": level_2,
                    "level-3": level_3,
                    "level-4": level_4,
                    "level-5": level_5,
                    "level-6": "any",
                }
            ]
        )
        cap_df = pd.concat([cap_df, df], ignore_index=True)

    breakpoint()
    cap_df.to_csv("capital_gain_taxonimy_tree.csv", index=False)

    breakpoint()
