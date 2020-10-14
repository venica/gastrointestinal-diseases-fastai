import os
import shutil
import random

# Se establece el directorio en el que están todas las imágenes deseadas
os.chdir('C:\\Users\\veron\\Escritorio\\CITIC\\CREACIÓN DEL DATASET\\Dataset\\Polyps')

# Se establecen los directorios destino para separar las imágenes en train y valid
train_dir = 'C:\\Users\\veron\\Escritorio\\CITIC\\CREACIÓN DEL DATASET\\Dataset_valid_train\\train\\Polyps'
valid_dir = 'C:\\Users\\veron\\Escritorio\\CITIC\\CREACIÓN DEL DATASET\\Dataset_valid_train\\valid\\Polyps'

# Se crea una lista con todas las imágenes del directorio en el que se están todas las imágenes
imagenes = os.listdir('.')

# Se crea una semilla y se aleatoriza la lista según dicha semilla
random.seed(4444)
random.shuffle(imagenes)

# Se calcula el número de imágenes que van a ir para train y para valid, respectivamente
train_num = round(0.8*len(imagenes)) # Se hace round porque no puede copiarse media imagen
valid_num = len(imagenes) - train_num

## Para la clase de Normal ##
# train_num = 800 
# valid_num = 200

# print (valid_num)
# print (train_num)
# print (imagenes)

# Se crean dos nuevas listas, una para train que incluirá el 80% de las imágenes originales y una para valid que incluirá el restante 20%
train_im = imagenes[:train_num]
valid_im = imagenes[train_num:]

## Para la clase de Normal ##
# train_im = imagenes[:train_num]
# valid_im = imagenes[train_num:train_num+valid_num]
# print(train_im)
# print(valid_im)

# Para cada imagen en train y valid, se hace que se copie de la carpeta original a la carpeta destino correspondiente
for i in train_im:
    shutil.copy(i, train_dir)

for x in valid_im:
    shutil.copy(x, valid_dir)

# Se imprime por pantalla cuantas imágenes se copian para train y valid
print (train_num, 'imágenes serán copiadas para train')
print (valid_num, 'imágenes serán copiadas para validation')