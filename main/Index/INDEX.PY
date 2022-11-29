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
tamanio = 1, 2, 3

marca = "garret", "kkk", "mitsubishi", "toyota", "borg warner" , "ihi" , "holset"

zona = 1,2,3,4

#index

#tamanio = input("ingrese tamanio")
#print("usted quiere" + tamanio)

#marca = input("ingrese marca")
#print ("usted quiere" + marca)

#zona = input("ingrese zona")
#print ("usted eligio" + zona)

#El usuario debe ingresar los datos del turbo
#Verificar si el mismo esta disponible

#ingresar los datos para veridicar si son correctos

eleccion = 0
eleccion2 = 0

quiereComenzar = Y,N

continuamos = Y,N


#Variable de contabilidad
cuentaMarca = 0

cuentaTamanio = 0

cuentaModeloTotal = cuentaMarca
cuentaTalleTotal = cuentaTamanio

while True:
  quiereComenzar = input('¿Comenzamos? / ¿Seguir?')
  if quiereComenzar !=N:

    while eleccion !=4:
        print("Indique tamaño deseado 1 pulgada, 2 pulgadas o 3 pulgadas")
        eleccion = int(input())
   
        if eleccion == 1 :
            print("1 pulgada")
            break


        if eleccion == 2 :
            print("2 pulgadas")
            break


        if eleccion == 3 :
            print("3 pulgadas")
            break

        continue
   

    while True:
        print("Marcas disponibles kkk, garret, mitsubishi, toyota, borg warner, ihi, holset")
        marca = input("Ingrese marca")
    
        if marca != "kkk" and marca != "garret" and marca != "mitsubishi" and marca != "toyota" and marca != "borg warner" and marca != "ihi" and marca != "holset" :
            print("Eliga marca valida")
        else:
            print("Marca valida")
            break
        continue

    while eleccion2 != 5:
        print("Ingrese zona deseada: 1 Norte, 2 Sur, 3 Este o 4 Oeste")
        eleccion2 = int(input())
    
        if eleccion2 == 1 :
            print("Zona Norte, proxima entrega en 24hs")
            break

        if eleccion2 == 2 :
            print("Zona Sur, proxima entrega en 48hs")
            break

        if eleccion2 == 3 :
            print("Zona Este, proxima entrega en 3 dias")
            break

        if eleccion2 == 4 :
            print("Zona Oeste, proxima entrega en 4 dias")
            break

        continue

    while True:
        if marca == "kkk" or marca== "garret" or marca == "mitsubishi" or marca == "toyota" :
         cuentaMarca+=1
         print(cuentaMarca)
         break
        continue
    while True:    
        if eleccion == 2 or eleccion == 1 or eleccion == 3 :
         cuentaTamanio+=1
         print(cuentaTamanio)
         break  
        else:
            print("¿Y entonces qué queres?")
    break


while True:
    continuamos = print("¿Quiere continuar?")
    if continuamos == Y:
      quiereComenzar()
    else:
      print("muchas gracias")
      break
    continue



#FechaEntrega

"calendar"

import calendar
 
fecha = calendar.TextCalendar(
    calendar.SUNDAY)

print(fecha.prmonth (2022, 11))

#VARIABLEUSUARIO

import openpyxl


#definimos la ubicacion del archivo

wb = openpyxl.load_workbook('C:\Desarrollo\Excel\Basse de datos Turbo.xlsx')

print(wb.sheetnames)

ws = wb['Clientes']

