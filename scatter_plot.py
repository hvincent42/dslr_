import utils
import matplotlib.pyplot as plt
import pandas as pd


def scatter_plot_single(feature1: str, feature2: str, data: pd.DataFrame) -> None:
    """
    Generate a scatter plot of the data for comparison between two features.
    
    Args:
        course1 (str): The first course to compare.
        course2 (str): The second course to compare.
        data (pd.DataFrame): The DataFrame containing the data.
    """
    houses = data['Hogwarts House'].unique()
    houses_color = {
        'Gryffindor': 'red',
        'Hufflepuff': 'yellow',
        'Ravenclaw': 'blue',
        'Slytherin': 'green'
    }
    plt.figure(figsize=(7, 7))
    for house in houses:
        house_data1 = data[data['Hogwarts House'] == house]
        plt.scatter(house_data1[feature1], house_data1[feature2], color=houses_color[house], alpha=0.7)

    plt.legend(houses, loc='upper left', frameon=False, title='Hogwarts Houses', title_fontsize='large')
    plt.title(f'Scatter plot of {feature1} vs {feature2}')
    plt.xlabel(feature1)
    plt.ylabel(feature2)
    plt.show()


if __name__ == '__main__':
    data = utils.load_csv('datasets/dataset_train.csv')
    #scatter_plot(data)
    scatter_plot_single('Arithmancy', 'Care of Magical Creatures', data)