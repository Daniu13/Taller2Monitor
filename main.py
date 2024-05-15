"""Daniel Iván Lozano Simanca
Andrés Camilo Bastidas
Info II grupos de Yesid (somos de grupos diferentes)"""


import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import pydicom
import nibabel as nib
import dicom2nifti as d2n
import shutil

def mostrar_plt(imagen, cmap='gray'):
    plt.imshow(imagen, cmap=cmap, vmin=0, vmax=255)

def varias_plt(imagen, neu, cmap):
    #neu = imagen=cambio_color(imagen)
    plt.subplot(1,2,1)
    mostrar_plt(imagen, cmap)
    plt.title("Imagen BRG")

    plt.subplot(1,2,2)
    mostrar_plt(neu, cmap)
    plt.title("Imagen Conteo")
    plt.show()

def play_opencv():
    if os.path.exists('img_cell.jpg'): 
        img_cell = cv2.imread('img_cell.jpg')
        img_cell = cv2.cvtColor(img_cell, cv2.COLOR_BGR2RGB)

        img_cellR = img_cell[:,:,2]
        _, imgB = cv2.threshold(img_cellR, 90, 255, cv2.THRESH_BINARY)
        kernel = np.ones((13,13), np.uint8)
        kernel1 = np.ones((15,15), np.uint8)
        imaDil = cv2.dilate(imgB, kernel, iterations = 1)
        imaEro = cv2.erode(imaDil,kernel1,iterations = 1)

        contours, _ = cv2.findContours(imaEro, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        num_celulas = len(contours)
        print("Número de células identificadas:", num_celulas)

        varias_plt(img_cell, imaEro, cmap='gray')

    else:
        print('El archivo no existe.')


"""Preguntar a Yesid"""
def parte_dicom():
    if os.path.exists('archivosDCM'):
        archivos_dicom = [archivo for archivo in os.listdir('archivosDCM') if archivo.endswith('.dcm')]
        archivos_dicom.sort()
        imagenes_dicom = [pydicom.dcmread(os.path.join('archivosDCM', archivo)) for archivo in archivos_dicom]
        for img in imagenes_dicom:
            plt.imshow(img.pixel_array, cmap='gray')
            plt.title("Imagen DICOM")
            plt.show()
    else:
        print("La carpeta no existe.")

while True:
    print("Opciones:\n1- Parte opencv\n2- Parte dicom")
    menu = int(input("Elija una opción: "))
    if menu == 1:
        play_opencv()
    elif menu == 2:
        parte_dicom()
    else:
        print("valor no válido.")