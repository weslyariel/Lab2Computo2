# Keyla Nallely Canales Nuñez - SMTR068223
# Wesly Ariel Umanzor Arias - SMTR072723
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('2024BallonDor.csv')


# Filtrar los jugadores con edades entre 16 y 30 años
filtered_dataset = dataset[(dataset['age'] >= 16) & (dataset['age'] <= 30)]

# Tomar solo los primeros 10 jugadores
top_10_players = filtered_dataset.head(10)

# Crear el gráfico lineal
plt.figure(figsize=(12, 6))  # Tamaño del gráfico
plt.plot(top_10_players['player'], top_10_players['age'], marker='o', color='blue', linestyle='-', linewidth=2, markersize=6)

# Títulos y etiquetas
plt.title('Edad de los Primeros 10 Jugadores Nominados al Balón de Oro 2024 (16-30 años)', fontsize=16, pad=20)
plt.xlabel('Jugador', fontsize=14)
plt.ylabel('Edad', fontsize=14)
plt.xticks(rotation=45, fontsize=10)  # Rotar etiquetas del eje X para mejor legibilidad
plt.yticks(fontsize=12)  # Tamaño de fuente de las etiquetas del eje Y
plt.grid()  # Añadir una cuadrícula
plt.tight_layout()  # Ajustar el diseño para que no se solapen etiquetas
plt.show()