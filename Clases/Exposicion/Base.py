import pandas as pd
import plotly.express as px

# Leer el dataset
dataset = pd.read_csv('C:/Users/Jhosep/Desktop/Diplomado/Clases/exposicion/owid-covid-data.csv')

# Filtrar las columnas necesarias
data_filtrada = dataset[['continent', 'location', 'date', 'total_deaths']]

# Convertir la columna 'date' a formato de fecha
data_filtrada['date'] = pd.to_datetime(data_filtrada['date'])

# Filtrar los datos para los países de América Latina
lista_paises = ['Argentina', 'Peru', 'Paraguay', 'Brazil', 'Chile', 'Uruguay', 
                'Colombia', 'Ecuador', 'Bolivia', 'Venezuela']

data_latam = data_filtrada[data_filtrada['location'].isin(lista_paises)]

# Filtrar los datos desde el año 2020 en adelante
data_latam = data_latam[data_latam['date'].dt.year >= 2020]

# Crear una nueva columna 'year' para agrupar por año
data_latam['year'] = data_latam['date'].dt.year

# Eliminar filas con valores nulos en 'total_deaths'
data_latam_limpio = data_latam.dropna(subset=['total_deaths'])

# Agrupar los datos por año y país, sumando las muertes totales por año
data_agrupada = data_latam_limpio.groupby(['location', 'year'], as_index=False)['total_deaths'].sum()

# Crear gráfico de líneas con Plotly
fig = px.line(data_agrupada, x='year', y='total_deaths', color='location',
              title='Aumento de Muertes por COVID-19 en Latinoamérica (2020 en adelante)',
              labels={'total_deaths': 'Total de Muertes', 'year': 'Año', 'location': 'Países'})

# Mostrar el gráfico
fig.show()
