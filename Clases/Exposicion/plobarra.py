import pandas as pd
import plotly.express as px

# Leer el dataset
dataset = pd.read_csv('C:/Users/Jhosep/Desktop/Diplomado/Clases/exposicion/owid-covid-data.csv')

# Lista de países de América Latina
lista_paises = ['Argentina', 'Peru', 'Paraguay', 'Brazil', 'Chile', 'Uruguay', 
                'Colombia', 'Ecuador', 'Bolivia', 'Venezuela']

# Filtrar los datos solo para esos países
data_latam = dataset[dataset['location'].isin(lista_paises)]

# Seleccionar columnas relevantes
data_barras = data_latam[['location', 'total_cases']].dropna()

# Crear gráfico de barras usando Plotly
fig = px.bar(data_barras, x='location', y='total_cases', title='Casos Totales en Latinoamérica')

# Mostrar el gráfico
fig.update_layout(xaxis_tickangle=-45)  # Rotar las etiquetas del eje X
fig.show()
