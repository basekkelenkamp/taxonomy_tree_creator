import pandas as pd

STEPS = [0, 200_000, 600_000]
counts = [0] * len(STEPS)


def calculate_row_range(row_, level):
    step = STEPS[level]
    counts[level] += 1
    if counts[level] >= step:
        counts[level] = 0

    return f"{row_ - counts[level]}-{row_ - counts[level] + step}"


if __name__ == "__main__":
    adult_df = pd.read_csv("input-data/adult-dataset.csv")
    fnlwgt = adult_df["fnlwgt"].unique()

    rows = sorted(fnlwgt.tolist())
    fnlwgt_df = pd.DataFrame(columns=[f"level-{i}" for i, step in enumerate(STEPS)])

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
        fnlwgt_df = pd.concat([fnlwgt_df, df], ignore_index=True)

    filename = "output-data/scenario-b-coarse-tax-fnlwgt.csv"
    print(f"Filename: {filename}")
    print("generate tree? ('y' or 'n')")

    if 'y' in input():
        fnlwgt_df.to_csv(filename, index=False)

    breakpoint()
