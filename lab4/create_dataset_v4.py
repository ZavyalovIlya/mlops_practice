import pandas as pd

df = pd.read_csv('titanic.csv')
df = df.head()
df.to_csv('titanic.csv', index=False)