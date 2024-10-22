import pandas as pd
import matplotlib.pyplot as plt
import random

# Cargar el archivo CSV con los datos
keyfacial_df = pd.read_csv('data.csv')

# Crear una figura grande con 64 subplots (8x8)
fig = plt.figure(figsize=(20, 20))

# Iterar 64 veces para dibujar cada imagen con sus puntos faciales
for i in range(64):
    # Escoger una fila aleatoria del DataFrame
    k = random.randint(0, len(keyfacial_df) - 1)
    
    # Crear un subplot en la posición correspondiente
    ax = fig.add_subplot(8, 8, i + 1)
    
    # Dibujar la imagen en escala de grises
    image_data = eval(keyfacial_df['Image'][k])  # Si 'Image' está en forma de string, usamos eval()
    ax.imshow(image_data, cmap='gray')
    
    # Dibujar los puntos faciales en la imagen
    for j in range(1, 31, 2):
        x = keyfacial_df.iloc[k, j - 1]  # Coordenada X
        y = keyfacial_df.iloc[k, j]      # Coordenada Y
        ax.plot(x, y, 'rx')  # Dibujar punto en rojo ('r') con una 'x'
    
    ax.axis('off')  # Ocultar los ejes para que solo se vea la imagen

# Guardar la figura como archivo PNG
fig.savefig('output.png')
print("Gráfica guardada como output.png")
