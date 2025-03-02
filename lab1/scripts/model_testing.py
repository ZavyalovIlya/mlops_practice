from sklearn.metrics import root_mean_squared_error as rmse
from func import pkl_read

# import test data and model
X_test= pkl_read('./data/test/X_test_std.pkl')
y_test = pkl_read('./data/test/y_test_std.pkl')

linreg = pkl_read('./models/linreg.pkl')
scaler_y = pkl_read('./models/scaler_y.pkl')

y_hat = linreg.predict(X_test)

print(f'+++++++ Test sample: RMSE is {round(rmse(scaler_y.inverse_transform(y_test), 
                                          scaler_y.inverse_transform(y_hat)), 2)}')
print('model testing successful')