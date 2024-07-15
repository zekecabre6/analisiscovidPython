import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Cargar el dataset
data = pd.read_csv('dataset.csv')

# Verificar las primeras filas del dataset
print(data.head())

# Resumen estadístico
print(data.describe())

# Correlaciones
correlation_matrix = data[['Confirmed', 'Deaths', 'Recovered']].corr()
print(correlation_matrix)

# Crear visualizaciones

# Matplotlib: Histograma de Casos Confirmados
plt.figure(figsize=(10, 6))
plt.hist(data['Confirmed'], bins=10, edgecolor='black')
plt.title('Histograma de Casos Confirmados')
plt.xlabel('Casos Confirmados')
plt.ylabel('Frecuencia')
plt.show()

# Plotly: Gráfico de Dispersión entre Casos Confirmados y Muertes
fig = px.scatter(data, x='Confirmed', y='Deaths', color='Country',
                 title='Gráfico de Dispersión de Casos Confirmados vs Muertes por País')
fig.show()

# Plotly: Gráfico de Línea de Casos Confirmados por Fecha para Todos los Países
fig = px.line(data, x='Date', y='Confirmed', color='Country',
              title='Casos Confirmados de COVID-19 por Fecha')
fig.show()

# Plotly: Gráfico de Línea de Muertes por Fecha para Todos los Países
fig = px.line(data, x='Date', y='Deaths', color='Country',
              title='Muertes por COVID-19 por Fecha')
fig.show()