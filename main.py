import pandas as pd

STEPS = [1, 2, 5, 10, 25, 50, 100]

counts = [0, 0, 0, 0, 0, 0, 0]


def calculate_row_range(step_range, count, row):
    if count == 0:
        return f"{row}-{row + STEPS[0]}"
    else:
        return f"{row - STEPS[0]}-{row}"


if __name__ == "__main__":
    adult_df = pd.read_csv("adult-dataset.csv")
    columns = adult_df.columns.tolist()
    breakpoint()
    #
    # rows = range(1, 100)
    # age_df = pd.DataFrame(columns=[f"level-{i}" for i, step in enumerate(STEPS, start=1)])
    # count = 0
    #
    # for row in rows:
    #     level_2 = calculate_row_range(STEPS[0], count, row)
    #
    #     df = pd.DataFrame(
    #         [
    #             {
    #                 "level-1": str(row),
    #                 "level-2": level_2,
    #                 "level-3": "",
    #                 "level-4": "",
    #                 "level-5": "",
    #                 "level-6": "",
    #                 "level-7": "any",
    #             }
    #         ]
    #     )
    #     age_df = pd.concat([age_df, df], ignore_index=True)
    #
    # breakpoint()
    # age_df.to_csv("age_taxonimy_tree.csv", index=False)
    #
    # breakpoint()
