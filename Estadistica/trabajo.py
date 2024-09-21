import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv('C:/Users/Jhosep/Desktop/Diplomado/Estadistica/Base_financiera_f.csv')

data_filtrada = dataset[['ID','Edad','Estado_civil','Zona_geografica','Ingreso','Tenencia_Saldo_rcc','Cantidad_productos_rcc','Target_mora']]

data_limpia = data_filtrada.dropna()

data_limpia['Zona_geografica'] = data_limpia['Zona_geografica'].str.strip()

#data_columnas = data_limpia['Zona_geografica'].unique()

data_barras = data_limpia[['Zona_geografica','Ingreso']]

plt.figure(figsize=(14,6))
barplot = sns.barplot(data=data_barras,x='Zona_geografica',y='Ingreso')

plt.xticks(rotation = 45)
plt.title('Ingresos por Zona Geografica')
plt.show()
