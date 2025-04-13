from catboost.datasets import titanic

titanic_train, titanic_test = titanic()
df = titanic_train[['Pclass', 'Sex', 'Age']]
df.to_csv('titanic.csv', index=False)