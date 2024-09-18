import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Leer el dataset
dataset = pd.read_csv('C:/Users/Jhosep/Desktop/Diplomado/Clases/exposicion/owid-covid-data.csv')

# Filtrar los datos solo para Brazil
data_brazil = dataset[dataset['location'] == 'Brazil']

# Convertir la columna de fecha a formato datetime
data_brazil['date'] = pd.to_datetime(data_brazil['date'])

# Filtrar columnas relevantes
data_lineas = data_brazil[['date', 'new_cases']].dropna()

# Crear gráfico de líneas para Brazil
plt.figure(figsize=(10,6))
sns.lineplot(data=data_lineas, x='date', y='new_cases', label='Brazil')
plt.title('Evolución de Nuevos Casos en Brazil')
plt.ylabel('Nuevos Casos')
plt.xlabel('Fecha')
plt.xticks(rotation=45)
plt.legend()
plt.show()
