import cv2
import numpy as np
import sys
from matplotlib import pyplot as plt

def activeChannel(imagePath):
    
    print("inicia el proceso de generacion de imagen")

    img = cv2.imread(imagePath)
    color = ('b','g','r')
    
    for i,col in enumerate(color):
        histograma = cv2.calcHist([img],[i],None,[256],[0,256])
        plt.plot(histograma,color = col)
        plt.xlim([0,256])
    plt.show()

    print("Finalizo la generacion de la imagen!!")

activeChannel("naruto.jpeg")
