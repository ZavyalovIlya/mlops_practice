from sklearn.datasets import fetch_california_housing
import pandas as pd

# downloading the dataset
df = fetch_california_housing()
X = pd.DataFrame(df.data, columns=df.feature_names)
y = pd.DataFrame(df.target, columns=df.target_names)

# export data to data/raw directory
X.to_csv('./data/raw/X.csv', index=False)
y.to_csv('./data/raw/y.csv', index=False)

print('data creation successful')
