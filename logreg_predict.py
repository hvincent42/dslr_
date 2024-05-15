import numpy as np
import pandas as pd
import json
from sklearn.preprocessing import MinMaxScaler
import utils_h as utils


def scale_columns(data):
    
    scaler = MinMaxScaler(feature_range=(0, 10))

    for column in data.columns:
        data[column] = scaler.fit_transform(data[[column]])

    return data


def load_dataset(filename):
    df = pd.read_csv(filename)
    X = df.values
    return X

def load_weights(filename):
    with open(filename, 'r') as f:
        weights_and_biases = json.load(f)
    weights = [np.array(w) for w in weights_and_biases['weights']]
    biases = weights_and_biases['biases']
    return weights, biases

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def predict(X, weights, biases):
    predictions = []
    for i, w in enumerate(weights):
        linear_model = np.dot(X, w) + biases[i]
        predictions.append(sigmoid(linear_model))
    predictions = np.array(predictions).T
    predicted_class = np.argmax(predictions, axis=1)
    return predicted_class


def save_predictions(predictions, filename):
    house_mapping = {0: 'Gryffindor', 1: 'Hufflepuff', 2: 'Ravenclaw', 3: 'Slytherin'}
    house_predictions = [house_mapping[pred] for pred in predictions]
    df = pd.DataFrame(house_predictions, columns=['Predicted House'])
    df.to_csv(filename, index=True, header=False)

    with open(filename, 'r') as file:
        house_pred = file.readlines()
        house_pred = ["Index, Hogwarts House" + '\n'] + house_pred
    with open(filename, 'w') as file:
        file.writelines(house_pred)



weights, biases = load_weights('weights.json')
df = pd.read_csv("data/dataset_test.csv")
X_test = df.drop(['Index', 'Hogwarts House', 'First Name', 'Last Name', 'Birthday', 'Best Hand', 'Arithmancy', 'Potions', 'Care of Magical Creatures'], axis=1)
X_test = utils.replaceNanWithMean(X_test)
X_test = scale_columns(X_test)
predictions = predict(X_test, weights, biases)


save_predictions(predictions, 'houses.csv')

