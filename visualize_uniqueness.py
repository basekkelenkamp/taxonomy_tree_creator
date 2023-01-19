import pandas as pd
import matplotlib.pyplot as plt


if __name__ == "__main__":
    results_df = pd.read_csv('output-data/uniqueness-3.6/uniqueness_results.csv')

    for i, row in results_df.iterrows():
        # Create a figure and two subplots
        fig, ax1 = plt.subplots()
        ax2 = ax1.twinx()
        # Create the first bar for the amount
        ax1.bar(['amount'], row['Amount of unique records'], label='Amount of unique records')
        ax1.set_ylabel('Amount')
        # Create the second bar for the percentage
        ax2.bar(['percentage'], row['Percentage unique records'], label='Percentage unique records')
        ax2.set_ylabel('Percentage')
        # Set the range for the percentage y-axis
        ax2.set_ylim(0, 100)
        plt.xlabel('Amount, Percentage')
        plt.suptitle("Record uniqueness", fontsize=16)
        plt.title(row['experiment'], fontsize=10)
        # Add the value of the amount and percentage inside the bars
        ax1.annotate(row['Amount of unique records'], ('amount', row['Amount of unique records']), ha='center',
                     va='bottom')
        ax2.annotate(str(row['Percentage unique records']) + '%', ('percentage', row['Percentage unique records']), ha='center',
                     va='bottom')

        ax2.set_yticklabels([f"{int(y)}%" for y in ax2.get_yticks()])

        # # Add legend
        # ax1.legend(loc="upper left")
        # ax2.legend(loc="upper right")
        plt.show()