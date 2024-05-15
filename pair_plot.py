import utils
import matplotlib.pyplot as plt
import seaborn as sns
# import plotly as px
import pandas as pd


def pair_plot(data: pd.DataFrame) -> None:
    """
    Generate a pair plot of the data.
    
    Args:
        data (pd.DataFrame): The DataFrame containing the data.
    """


    grouped = data.groupby('Hogwarts House')


    gryffindor = grouped.get_group('Gryffindor')
    hufflepuff = grouped.get_group('Hufflepuff')
    ravenclaw = grouped.get_group('Ravenclaw')
    slytherin = grouped.get_group('Slytherin')

    colors = ['cyan', 'purple', 'blue', 'green']

    features = gryffindor.columns[6:]

    columns = list(features) + ['Hogwarts House']
    plt.rcParams['axes.labelsize'] = 7

    plot = sns.pairplot(data[columns], hue='Hogwarts House', height=0.8, plot_kws={'s': 7})
    plot._legend.set_title('Hogwarts House')
    for label in plot._legend.texts:
        label.set_fontsize(7)
    plot._legend.get_title().set_fontsize(7)
    # plt.title('Pair plot of Hogwarts Houses Marks')
    plt.show()


if __name__ == "__main__":
    data = utils.load_csv('datasets/dataset_train.csv')
    pair_plot(data)


