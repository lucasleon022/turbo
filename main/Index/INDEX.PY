#################################################
# Primer Commit main Turbo
# *Subir a Github
# * Index.py
# ejecutable.exe
# release: 26/10/2022
# developer: Lucas Leon
################################################

from ast import While
from cgitb import reset
from operator import concat
from tkinter import N, Y

#VARIABLES
tamanio = 22.4, 44.8, 67.2

marca = "GARRET", "KKK", "MITSUBISHI", "T0YOTA", "BORG WARNER" , "Ihi" , "HOLSET"

zona = 1,2,3,4

#index

tamanio = input("ingrese tamanio")
print("usted quiere" + tamanio)

marca = input("ingrese marca")
print ("usted quiere" + marca)

zona = input("ingrese zona")
print ("usted eligio" + zona)

#El usuario debe ingresar los datos del turbo
#Verificar si el mismo esta disponible

#ingresar los datos para veridicar si son correctos


while True:
    tamanio = int(input("Ingrese tamanio"))
    if tamanio != 22.4 :
        print("Escriba un tamanio valido")
    else:
        print("Tamanio valido")
        break
    continue

while True:
    marca = input("Ingrese marca")
    if marca != "GARRET":
        print("Eliga marca valida")
    else:
        print("Marca valida")
        break
    continue

while True:
    zona = int(input("Ingrese zona"))
    if zona != 1 :
        print("Zona invalida, ingrese zona valida")
    else:
        print("Zona valida")
        break
    continue
