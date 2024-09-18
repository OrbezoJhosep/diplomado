import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

dataset = pd.read_csv('C:/Users/Jhosep/Desktop/Diplomado/Clases/exposicion/owid-covid-data.csv')

lista_paises = ['Argentina', 'Peru', 'Paraguay', 'Brazil', 'Chile', 'Uruguay', 
                'Colombia', 'Ecuador', 'Bolivia', 'Venezuela']

#filtrar
data_latam = dataset[dataset['location'].isin(lista_paises)]

#seleccionar

data_barras = data_latam[['location','total_cases']]

plt.figure(figsize=(20,10))
barplot = sns.barplot(data = data_barras, x = 'location', y = 'total_cases')


plt.xticks(rotation = 45)
plt.title ('Casos en latinoamerica')
plt.show()



