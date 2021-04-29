# Dataset empleado para el entrenamiento del modelo

## Links de interés

* Dataset original --> Kvasir Dataset (https://datasets.simula.no/kvasir/)
  * Konstantin Pogorelov, Kristin Ranheim Randel, Carsten Griwodz, Sigrun Losada Eskeland, Thomas de Lange, Dag Johansen, Concetto Spampinato, Duc-Tien Dang-Nguyen, Mathias Lux, Peter Thelin Schmidt, Michael Riegler, Pål Halvorsen, Kvasir: A Multi-Class Image Dataset for Computer Aided Gastrointestinal Disease Detection, In MMSys'17 Proceedings of the 8th ACM on Multimedia Systems Conference (MMSYS), Pages 164-169 Taipei, Taiwan, June 20-23, 2017.

* Dataset con los bordes recortados --> https://udcgal-my.sharepoint.com/:f:/g/personal/veronica_aranda_udc_es/Eu1D0PEfUlNIu-mUT2-CBpsBw3LQcxktQfOdcccgD0FPQA?e=hMai5x
* Dataset dividido en train y valid --> https://udcgal-my.sharepoint.com/:f:/g/personal/veronica_aranda_udc_es/EvSAPNfqqRtKjhzoMmrW4ykBYqhYI_jMZ4Ndx0uhhDPquQ?e=HSJ4aW


## Códigos empleados

* [Renombrar.py](Renombrar.py) --> Se empleó para renombrar las imágenes y que fuera más fácil trabajar con ellas e identificarlas, por si al emplear el código [Recorte.py](Recorte.py) (que se va a explicar a continuación) se produjera algún error o no diera el resultado esperado/deseado en alguna de ellas. 

* [Recorte.py](Recorte.py) --> Se empleó para recortar el borde negro de las imágenes para quitar en lo máximo de lo posible información no importante para el entrenamiento del modelo. 

* [Split.py](Split.py) --> Se empleó para dividir el dataset en dos carpetas: train y valid. 
