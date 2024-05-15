import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

from log_regression_ova import LogisticRegressionOvA
import utils_h as utils

def scale_columns(data):
    
    scaler = MinMaxScaler(feature_range=(0, 10))

    for column in data.columns:
        data[column] = scaler.fit_transform(data[[column]])

    return data


df = pd.read_csv("data/dataset_train.csv")


X_train = df.drop(['Index', 'Hogwarts House', 'First Name', 'Last Name', 'Birthday', 'Best Hand', 'Arithmancy', 'Potions', 'Care of Magical Creatures'], axis=1)
X_train = utils.replaceNanWithMean(X_train)
X_train = scale_columns(X_train)
y_train = df['Hogwarts House']


clf = LogisticRegressionOvA()
clf.fit(X_train, y_train)
loss = clf.calculate_loss(X_train, y_train)            
print("Loss: ", loss)
clf.save_weights()
