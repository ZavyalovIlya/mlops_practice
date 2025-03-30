from sklearn.datasets import fetch_california_housing
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import pickle

def pkl_dump(path, model):
    with open(path, 'wb') as file:
        pickle.dump(model, file)

# downloading the dataset
df = fetch_california_housing()
X = df.data.reshape(20640, 8)
y = df.target.reshape(20640, 1)

# data standardization
scaler_X = StandardScaler()
scaler_X.fit(X)
X = scaler_X.transform(X)

scaler_y = StandardScaler()
scaler_y.fit(y)
y = scaler_y.transform(y)

# train model
linreg = LinearRegression().fit(X, y)

# save model
pkl_dump('backend/models/linreg.pkl', linreg)

pkl_dump('backend/models/scaler_X.pkl', scaler_X)
pkl_dump('backend/models/scaler_y.pkl', scaler_y)