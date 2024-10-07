# Keyla Nallely Canales Nuñez - SMTR068223
# Wesly Ariel Umanzor Arias - SMTR072723
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('MarvelVsDC.csv')

# Contar las películas por género
genre_counts = dataset['Genre'].value_counts()

# Seleccionar los 7 géneros más comunes
top_7_genres = genre_counts.head(7)

# Gráfico de barras
plt.figure(figsize=(10, 6))
colores = ["yellow", "orange", "green", "purple", "blue", "red","black"]
top_7_genres.plot(kind='bar', color=colores)
plt.title('Top 7 Géneros de Películas')
plt.xlabel('Género')
plt.ylabel('Cantidad de Películas')
plt.xticks(rotation=45)  # Rotar las etiquetas del eje X para que se lean mejor
plt.grid(axis='y')  # Añadir cuadrícula en el eje Y

plt.tight_layout() 
plt.show()