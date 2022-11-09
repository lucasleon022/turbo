#VARIABLES TAMANIOS

import importlib


tamanio=1, 2, 3

#VARIABLES MARCAS

marca= "garret", "kkk", "mitsubishi", "toyota", "borg warner" , "ihi" , "holset"

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

#calendario para seleccionar mes en espesifico

import calendar
 
fecha = calendar.TextCalendar(
    calendar.SUNDAY)

print(fecha.prmonth (2022, 11))

#segunda forma hecha para imprimir todo el año


#Instancia de TextCalendar
anio_entero = calendar.TextCalendar()

#Elegimos el formato del año
calendario_2022 = anio_entero.formatyear(2022)

#Mostramos el resultado
print(calendario_2022)