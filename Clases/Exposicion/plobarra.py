import pandas as pd
import plotly.express as px

# Leer el dataset
dataset = pd.read_csv('C:/Users/Jhosep/Desktop/Diplomado/Clases/exposicion/owid-covid-data.csv')

# Filtrar las columnas necesarias
data_filtrada = dataset[['continent', 'location', 'date', 'total_cases', 'total_deaths']]

# Lista de países de América Latina
lista_paises = ['Argentina', 'Peru', 'Paraguay', 'Brazil', 'Chile', 'Uruguay', 
                'Colombia', 'Ecuador', 'Bolivia', 'Venezuela']

# Filtrar los datos para los países de la lista
data_latam = data_filtrada[data_filtrada['location'].isin(lista_paises)]

# Eliminar filas con valores nulos en 'total_cases'
data_latam_limpio = data_latam.dropna(subset=['total_cases'])

# Filtrar las columnas necesarias para el gráfico de barras
data_barras = data_latam_limpio[['location', 'total_cases']]

# Crear gráfico de barras con Plotly y personalización de colores
fig = px.bar(data_barras, x='location', y='total_cases', 
             title='Casos Totales en Latinoamérica',
             labels={'total_cases':'Casos Totales', 'location':'Países'},
             color_discrete_sequence=['#ADD8E6'])  # Barras de color azul claro

# Personalizar el color de fondo
fig.update_layout(
    plot_bgcolor='rgba(50, 50, 50, 1)',  # Fondo oscuro
    paper_bgcolor='rgba(50, 50, 50, 1)',  # Fondo del gráfico (canvas)
    font_color='white'  # Color del texto
)

# Rotar las etiquetas del eje X
fig.update_layout(xaxis_tickangle=-45)

# Mostrar el gráfico
fig.show()
