import numpy as np
import json

def sigmoid(x):
    x = np.clip(x, -500, 500)
    return 1 / (1 + np.exp(-x))

class LogisticRegressionOvA():

    def __init__(self, lr=0.0001, n_iters=10000):
        self.lr = lr
        self.n_iters = n_iters
        self.weights = []
        self.bias = []

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.classes = np.unique(y)

        for c in self.classes:
            y_c = np.where(y == c, 1, 0)
            weights_c = np.zeros(n_features)
            bias_c = 0

            for _ in range(self.n_iters):
                linear_pred = np.dot(X, weights_c) + bias_c
                y_predicted = sigmoid(linear_pred)
        
                gradient_weights = (1 / n_samples) * np.dot(X.T, (y_predicted - y_c))
                gradient_bias = (1 / n_samples) * np.sum(y_predicted - y_c)

                weights_c -= self.lr * gradient_weights
                bias_c -= self.lr * gradient_bias

            self.weights.append(weights_c)
            self.bias.append(bias_c)

    def save_weights(self):
        weights_and_biases = {'weights': [w.tolist() for w in self.weights], 'biases': self.bias}

        file_name = 'weights.json'

        with open(file_name, 'w') as f:
            json.dump(weights_and_biases, f)