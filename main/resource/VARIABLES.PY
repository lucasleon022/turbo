#VARIABLES TAMANIOS

import importlib


tamanio=22.4, 44.8, 67.2

#VARIABLES MARCAS

marca= "GARRET" , "KKK" , "MITSUBISHI" , "TOYOTA" , "BORG WARNER" , "Ihi" , "HOLSET"

#VARIABLES ZONA

zona= 1, 2, 3, 4

#VARIABLEUSUARIO

import openpyxl


#definimos la ubicacion del archivo

wb = openpyxl.load_workbook('C:\Desarroyo\Excel\basse de datos Turbo')

print(wb.sheetnames)

ws = wb.get_sheet_byname(name = 'Clientes')

#FechaEntrega

"calendar"