
import pandas as pd

# url = "https://raw.githubusercontent.com/selva86/datasets/master/Auto.csv"

# El método "read_csv" nos permite leer un csv
dataset = pd.read_csv('C:/Users/Jhosep/Desktop/Diplomado/Clases/taller1/titanic.csv')

#print(dataset.loc[(dataset['Pclass'] == 3) & (dataset['Survived'] == 0)])
#print(dataset.loc[(dataset['Age'] > 20) & (dataset['Survived']==1)])
#print(dataset.loc[(dataset['Pclass'] == 1) & (dataset['Survived']==0)])
#print(dataset.head())
print(dataset.loc[(dataset['Sex'] == 'female')])


