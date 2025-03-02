from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
from func import pkl_dump

# loading raw datasets
X = pd.read_csv('./data/raw/X.csv')
y = pd.read_csv('./data/raw/y.csv')

# split data into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.25,
                                                    random_state=42,
                                                    shuffle=True)

# data standardization
scaler_X = StandardScaler()
scaler_X.fit(X_train)
X_train, X_test = scaler_X.transform(X_train), scaler_X.transform(X_test)

scaler_y = StandardScaler()
scaler_y.fit(y_train)
y_train, y_test = scaler_y.transform(y_train), scaler_y.transform(y_test)

# export data and standardization models
pkl_dump('./data/train/X_train_std.pkl', X_train)
pkl_dump('./data/train/y_train_std.pkl', y_train)

pkl_dump('./data/test/X_test_std.pkl', X_test)
pkl_dump('./data/test/y_test_std.pkl', y_test)

pkl_dump('./models/scaler_X.pkl', scaler_X)
pkl_dump('./models/scaler_y.pkl', scaler_y)

print('data preprocessing successful')