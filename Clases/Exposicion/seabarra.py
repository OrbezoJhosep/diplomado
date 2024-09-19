import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv('C:/Users/Jhosep/Desktop/Diplomado/Clases/exposicion/owid-covid-data.csv')

#filtramos columna
data_filtrada = dataset[['continent','location','date','total_cases','total_deaths']] 

# paises que necesistamos
lista_paises = ['Argentina', 'Peru', 'Paraguay', 'Brazil', 'Chile', 'Uruguay', 'Colombia', 'Ecuador', 'Bolivia', 'Venezuela'] 

#filtramos columnas
data_latam = data_filtrada[data_filtrada['location'].isin(lista_paises)] 

#elimina nulos
data_latam_limpio = data_latam.dropna(subset=['total_cases'])

#data sin ceros
#data_latam_sin_ceros = data_latam[(data_latam['total_cases'] != 0)]

#grafico de barras
data_barras = data_latam_limpio[['location','total_cases']]

#Muestra en lienzo
plt.figure(figsize=(12,6))

barplopt = sns.barplot(data=data_barras, x='location', y='total_cases')

plt.xticks(rotation = 45)
plt.title('Casos en Latinoamerica')
plt.show()






