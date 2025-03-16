from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error as rmse

from func import pkl_dump, pkl_read

# import train data
X_train = pkl_read('data/train/X_train_std.pkl')
y_train = pkl_read('data/train/y_train_std.pkl')
scaler_y = pkl_read('models/scaler_y.pkl')

# train and evaluate model
linreg = LinearRegression().fit(X_train, y_train)
y_hat = linreg.predict(X_train)
print(f'+++++++ Train sample: R-sq is {round(linreg.score(X_train, y_train)*100, 2)}')
print(f'+++++++ Train sample: RMSE is {round(rmse(scaler_y.inverse_transform(y_train), 
                                          scaler_y.inverse_transform(y_hat)), 2)}')

# save model
pkl_dump('models/linreg.pkl', linreg)

print('model preparation successful')
