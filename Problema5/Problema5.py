import cv2
import numpy as np
import sys


def activeChannel(imagePath):
    
    print("inicia el proceso de generacion de imagen")

    img = cv2.imread(imagePath)
    
    alto = img.shape[0]
    ancho = img.shape[1]
    canales = img.shape[2]

    out =  np.zeros((alto, ancho, 3))
    
    
    for i in range (alto):
        for j in range(ancho):
            pixel = img[i,j]
            
            #formula de luminancia ponderada
            #Y = R*0.3+G*0.59+B*0.11
            gris_ponderado = int((int(pixel[0]*0.11) + int(pixel[1]*0.59) + int(pixel[2]*0.3)))
            
            out[i,j] = gris_ponderado
           

     # escribe la imagen en disco
    cv2.imwrite("salida.jpg",out)
    
    
    print("Finalizo la generacion de la imagen!!")

activeChannel("naruto.jpeg")