# Se cargan las librerÃ­as que se van a emplear
import cv2
import numpy as np
from matplotlib import pyplot as plt
from natsort import natsorted
import os

###### Se crea el bucle para que el cÃ³digo se ejecute para cada imÃ¡gen ######
imagenes = natsorted(os.listdir('C:\\Users\\veron\\Escritorio\\Hyperplasic selected'))
a = 0
for imagen in imagenes:
    os.chdir('C:\\Users\\veron\\Escritorio\\Hyperplasic selected')
    imc = cv2.imread(imagen)
    gray = cv2.cvtColor(imc,cv2.COLOR_BGR2GRAY)
    
    clahe = cv2.createCLAHE(clipLimit=4.5, tileGridSize=(2,2)) # Se realiza una ecualizaciÃ³n adaptativa del histograma mediante CLAHE
    gray = clahe.apply(gray)
    
    thr1, otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)
    er = cv2.morphologyEx(otsu, cv2.MORPH_CLOSE, np.ones((27,27))) # Eliminar ruido de la segmentación
 
    contours, hierarchy=cv2.findContours(er,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    out = imc * 1 # Copiamos la imagen original para no modificarla
    cv2.drawContours(out, contours, -1, (255,0,255), 4)
    
    select_contour = []
    for i in contours:
        if cv2.contourArea(i) > 100000:
            select_contour.append(i)
    
    if not select_contour:
        cnt = i
        x,y,w,h = cv2.boundingRect(cnt)
        crop = imc[y:y+h,x:x+w]

    else:
        cnt = select_contour[0]
        x,y,w,h = cv2.boundingRect(cnt)
        crop = imc[y:y+h,x:x+w]
    # C:\\Users\\veron\\Escritorio\\CITIC\\CREACIÓN DEL DATASET\\Dataset\\Normal
    newpath = 'C:\\Users\\veron\\Escritorio\\CITIC\\CREACIÓN DEL DATASET\\Dataset\\Hyperplasic Lesions' 
    os.chdir(newpath)
    
    cv2.imwrite('Hyperplasic selected crop' + str(a) + '.jpg', crop)     
    a = a + 1
