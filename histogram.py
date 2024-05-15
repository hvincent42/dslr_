import pandas as pd
import matplotlib.pyplot as plt
from utils_h import load_csv


def ft_histogram(data: pd.DataFrame) -> None:
    """
    Generate a histogram of the data.

    Args:
        data (pd.DataFrame): The DataFrame containing the data.
    """

    # Split the data into houses
    houses = data["Hogwarts House"].unique()
    houses_color = {
        "Gryffindor": "red",
        "Hufflepuff": "yellow",
        "Ravenclaw": "blue",
        "Slytherin": "green",
    }
    fig, axs = plt.subplots(4, 4, figsize=(20, 20))
    for house in houses:
        house_data = data[data["Hogwarts House"] == house]
        i = 0
        for column in house_data.columns:
            values = [x for x in house_data[column].values if not pd.isnull(x)]
            if all(isinstance(x, (int, float)) for x in values):
                axs[i // 4, i % 4].hist(values, bins=5, color=houses_color[house], alpha=0.5)
                axs[i // 4, i % 4].set_title(column)
                axs[i // 4, i % 4].set_xlabel("Marks")
                axs[i // 4, i % 4].set_ylabel("Frequency")
                i += 1

    for i in range(3): axs[3, i + 1].set_visible(False)
    fig.legend(houses, loc="lower right", frameon=False, title="Hogwarts Houses", title_fontsize="large")
    fig.suptitle("Histogram of Hogwarts Houses Marks", fontsize=20)
    plt.subplots_adjust(hspace=0.7)
    plt.show()


if __name__ == "__main__":
    data = load_csv("datasets/dataset_train.csv")
    ft_histogram(data)
