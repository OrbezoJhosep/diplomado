import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Leer el dataset completo
dataset = pd.read_csv('C:/Users/Jhosep/Desktop/Diplomado/Clases/exposicion/owid-covid-data.csv')

# Seleccionar las columnas relevantes y eliminar valores nulos
data_dispersion = dataset[['gdp_per_capita', 'total_cases_per_million']].dropna()

# Crear gráfico de dispersión
plt.figure(figsize=(10,6))
sns.scatterplot(data=data_dispersion, x='gdp_per_capita', y='total_cases_per_million')
plt.title('Relación entre PIB per cápita y Casos Totales por Millón')
plt.ylabel('Casos Totales por Millón')
plt.xlabel('PIB per cápita')
plt.show()
