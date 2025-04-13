import pandas as pd

df = pd.read_csv('titanic.csv')
df = pd.get_dummies(df, dtype=int)
df.to_csv('titanic.csv', index=False)