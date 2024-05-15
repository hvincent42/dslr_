import utils
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def scale_columns(data):
    scaler = MinMaxScaler(feature_range=(0, 10))

    for column in data.columns[6:]:
        data[column] = scaler.fit_transform(data[[column]])

    return data



data = pd.read_csv('datasets/dataset_train.csv')




data = scale_columns(data)

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

