# Dataset empleado para el entrenamiento del modelo

## Links de interés

* Dataset original --> Kvasir Dataset (https://datasets.simula.no/kvasir/)
* Dataset con los bordes recortados --> *insertar link*
* Dataset dividido en train y valid --> *insertar link*


## Códigos empleados

* [Renombrar.py](Renombrar.py) --> Se empleó para renombrar las imágenes y que fuera más fácil trabajar con ellas e identificarlas, por si al emplear el código [Recorte.py](Recorte.py) (que se va a explicar a continuación) se produjera algún error o no diera el resultado esperado/deseado en alguna de ellas. 

* [Recorte.py](Recorte.py) --> Se empleó para recortar el borde negro de las imágenes para quitar en lo máximo de lo posible información no importante para el entrenamiento del modelo. 

* [Split.py](Split.py) -->
