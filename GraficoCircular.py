# Keyla Nallely Canales Nuñez - SMTR068223
# Wesly Ariel Umanzor Arias - SMTR072723
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('spotify.csv')

# Filtrar el dataset para incluir solo las canciones de artistas latinoamericanos, (buscados por nombres)
filtered_dataset = dataset[dataset['artist(s)_name'].isin(['Feid', 'Myke Towers', 'Rauw Alejandro', 'Bad Bunny','Karol G', 'Ozuna',
                                                           'Manuel Turizo', 'Shakira', 'Don Omar', 'Daddy Yankee'])]

# Contar las canciones por artista
artist_counts = filtered_dataset['artist(s)_name'].value_counts()

# Crear un gráfico circular
plt.figure(figsize=(10, 10))  # Aumentar el tamaño del gráfico
plt.pie(artist_counts, labels=artist_counts.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.tab10.colors)
plt.title('Distribución de Canciones de artistas latinoamericanos en Spotify', fontsize=16, pad=30)  # Título del gráfico y con pad ajustamos el espaciado
plt.axis('equal')  # Para que el gráfico sea un círculo
plt.show()