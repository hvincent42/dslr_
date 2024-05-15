import utils
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def scatter_plot(data: pd.DataFrame) -> None:
    """
    Generate a scatter plot of the data.

    Args:
        data (pd.DataFrame): The DataFrame containing the data.
    """
    grouped = data.groupby('Hogwarts House')

    gryffindor = grouped.get_group('Gryffindor')
    hufflepuff = grouped.get_group('Hufflepuff')
    ravenclaw = grouped.get_group('Ravenclaw')
    slytherin = grouped.get_group('Slytherin')

    colors = ['cyan', 'purple', 'blue', 'green']
    # classes = gryffindor.columns


    groups = [gryffindor, hufflepuff, ravenclaw, slytherin]
    group_names = ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']
    # feature1 = data.columns[6]
    # feature2 = data.columns[7]

    # Create a new figure
    features = gryffindor.columns[6:]
    for i in range(0, len(features)):
    # Iterate over each group
        for j in range(i + 1, len(features)):
            plt.figure()
            for group, group_name, color in zip(groups, group_names, colors):
                    # Create a scatter plot for the current group
                    plt.scatter(group[features[i]], group[features[j]], label=group_name, color=color)
            plt.title(f'Scatter plot of {features[i]} vs {features[j]}')
            plt.xlabel(features[i])
            plt.ylabel(features[j])
            plt.legend()
            plt.show()


def scatter_plot_single(feature1: str, feature2: str, data: pd.DataFrame) -> None:
    """
    Generate a scatter plot of the data for comparison between two features.
    
    Args:
        course1 (str): The first course to compare.
        course2 (str): The second course to compare.
        data (pd.DataFrame): The DataFrame containing the data.
    """
    data1 = data[feature1]
    data2 = data[feature2]
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