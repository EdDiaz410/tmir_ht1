import cv2
import numpy as np
import sys

def activeChannel(imagePath):
    
    print("inicia el proceso de generacion de imagen")

    img = cv2.imread(imagePath)
    
    alto = img.shape[0]
    ancho = img.shape[1]
    canales = img.shape[2]

    outAzul =  np.zeros((alto, ancho, 1))
    outVerde =  np.zeros((alto, ancho, 1))
    outRojo =  np.zeros((alto, ancho, 1))
    
    for i in range (alto):
        for j in range(ancho):
            pixel = img[i,j]
            
            gris_azul = int((int(pixel[0]) + 0 + 0)/3)
            gris_verde = int((int(pixel[1]) + 0 + 0)/3)
            gris_rojo = int((int(pixel[2]) + 0 + 0)/3)

            outAzul[i,j] = gris_azul
            outVerde[i,j] = gris_verde
            outRojo[i,j] = gris_rojo

     # escribe la imagen en disco
    cv2.imwrite("salida_azul.jpg",outAzul)
    cv2.imwrite("salida_verde.jpg",outVerde)
    cv2.imwrite("salida_rojo.jpg",outRojo)
    
    print("Finalizo la generacion de la imagen!!")

activeChannel("naruto.jpeg")