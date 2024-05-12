"""Daniel Iván Lozano Simanca"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def mostrar_plt(imagen, cmap='gray'):
    plt.imshow(imagen, cmap=cmap, vmin=0, vmax=255)

def varias_plt(imagen, neu, cmap):
    #neu = imagen=cambio_color(imagen)
    plt.subplot(1,2,1)
    mostrar_plt(imagen, cmap)
    plt.title("Imagen RGB")

    plt.subplot(1,2,2)
    mostrar_plt(neu, cmap)
    plt.title("Imagen GRAY")
    plt.show()

if os.path.exists('img_cell.jpg'): 
    img_cell = cv2.imread('img_cell.jpg')
    img_cell = cv2.cvtColor(img_cell, cv2.COLOR_BGR2RGB)

    img_cellR = img_cell[:,:,2]
    Umb, imgB = cv2.threshold(img_cellR, 90, 255, cv2.THRESH_BINARY)
    kernel = np.ones((13,13),np.uint8)
    kernel1 = np.ones((15,15),np.uint8)
    imaDil = cv2.dilate(imgB, kernel, iterations = 1)
    imaEro = cv2.erode(imaDil,kernel1,iterations = 1)

    contours, _ = cv2.findContours(imaEro, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    num_celulas = len(contours)
    print("Número de células identificadas:", num_celulas)

    varias_plt(img_cell, imaEro, cmap='gray')

else:
    print('El archivo no existe.')