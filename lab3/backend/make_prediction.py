import pickle
import numpy as np

def pkl_read(path):
    with open(path, 'rb') as file:
        return pickle.load(file)

def main(X):

    X = np.reshape(X,(1, 8))

    #import models
    linreg = pkl_read('models/linreg.pkl')
    scaler_y = pkl_read('models/scaler_y.pkl')
    scaler_X = pkl_read('models/scaler_X.pkl')

    # transformations and prediction
    X = scaler_X.transform(X)
    y_hat = linreg.predict(X)
    y_hat = scaler_y.inverse_transform(y_hat)

    return round(y_hat[0][0], 2)

print(main([16.0,16.0,16.0,16.0,16.0,16.0,40.0, -120.0]))