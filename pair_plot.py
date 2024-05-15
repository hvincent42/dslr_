import utils
import matplotlib.pyplot as plt
import seaborn as sns
# import plotly as px
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def scale_columns(data):
    scaler = MinMaxScaler(feature_range=(0, 10))

    for column in data.columns[6:]:
        data[column] = scaler.fit_transform(data[[column]])

    return data



df = pd.read_csv('data/dataset_train.csv')




data = scale_columns(df)


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

# fig = px.scatter_matrix(data[columns], dimensions=features, color='Hogwarts House')
# plt.figure(figsize=(6, 6))
# plt.title(f'Pairplot of all houses')
plt.show() 



