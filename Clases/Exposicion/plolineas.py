import pandas as pd
import plotly.express as px

# Leer el dataset
dataset = pd.read_csv('C:/Users/Jhosep/Desktop/Diplomado/Clases/exposicion/owid-covid-data.csv')

# Filtrar los datos solo para Brazil
data_brazil = dataset[dataset['location'] == 'Brazil']

# Convertir la columna de fecha a formato datetime
data_brazil['date'] = pd.to_datetime(data_brazil['date'])

# Filtrar columnas relevantes
data_lineas = data_brazil[['date', 'new_cases']].dropna()

# Crear gráfico de líneas usando Plotly
fig = px.line(data_lineas, x='date', y='new_cases', title='Evolución de Nuevos Casos en Brazil', labels={
    'new_cases': 'Nuevos Casos',
    'date': 'Fecha'
})

# Rotar las etiquetas del eje X para mayor legibilidad
fig.update_layout(xaxis_tickangle=-45)

# Mostrar el gráfico interactivo
fig.show()
