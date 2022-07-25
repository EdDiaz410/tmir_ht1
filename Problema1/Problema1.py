import cv2
import numpy as np
import sys

def activeChannel(imagePath, color):
    
    print("inicia el proceso de generacion de imagen")

    img = cv2.imread(imagePath)
    
    alto = img.shape[0]
    ancho = img.shape[1]
    canales = img.shape[2]

    out =  np.zeros((alto, ancho, 3))
    gris =  np.zeros((alto, ancho, 1))

    for i in range (alto):
        for j in range(ancho):
            pixel = img[i,j]
            
            #azul
            if(color == 1): 
                colorSeleccionado = pixel[0] 
                out[i,j] = [colorSeleccionado, 0, 0]
            #verde
            elif(color == 2): 
                colorSeleccionado = pixel[1] 
                out[i,j] = [0, colorSeleccionado, 0]
            #rojo
            elif(color == 3): 
                colorSeleccionado = pixel[2] 
                out[i,j] = [0, 0, colorSeleccionado]
            #rojo y verde
            elif(color == 10):  
                colorSeleccionado = pixel[2]
                colorSeleccionado2 = pixel[1]
                out[i,j] = [0, colorSeleccionado, colorSeleccionado2]
            #verde y azul
            elif(color == 20):  
                colorSeleccionado = pixel[1]
                colorSeleccionado2 = pixel[0]
                out[i,j] = [colorSeleccionado2, colorSeleccionado, 0]
            #azul y rojo
            elif(color == 30):  
                colorSeleccionado = pixel[0]
                colorSeleccionado2 = pixel[2]
                out[i,j] = [colorSeleccionado, 0, colorSeleccionado2]
            

     # escribe la imagen en disco
    cv2.imwrite("salida.jpg",out)
    
    print("Finalizo la generacion de la imagen!!")

activeChannel("naruto.jpeg",30)