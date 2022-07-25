import cv2
import numpy as np
import sys

def activeChannel(imagePath1, imagePath2, imagePath3):
    
    print("inicia el proceso de generacion de imagen")

    imgRojo = cv2.imread(imagePath1)
    imgVerde = cv2.imread(imagePath2)
    imgAzul = cv2.imread(imagePath3)

    
    alto = imgRojo.shape[0]
    ancho = imgRojo.shape[1]
    canales = imgRojo.shape[2]

    out =  np.zeros((alto, ancho, 3))
    
    for i in range (alto):
        for j in range(ancho):
            pixelRojo = imgRojo[i,j]
            pixelVerde = imgVerde[i,j]
            pixelAzul = imgAzul[i,j]
            
            rojo = pixelRojo[2]
            verde = pixelVerde[1] 
            azul = pixelAzul[0]

            out[i,j] = [azul, verde, rojo]

     # escribe la imagen en disco
    cv2.imwrite("salida.jpg",out)
    
    print("Finalizo la generacion de la imagen!!")

activeChannel("imagen2_salida_gray_rojo.jpg","imagen2_salida_gray_verde.jpg","imagen2_salida_gray_azul.jpg")