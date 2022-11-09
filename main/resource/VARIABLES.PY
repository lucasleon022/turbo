#VARIABLES TAMANIOS

import importlib


tamanio=1, 2, 3

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

import calendar
 
fecha = calendar.TextCalendar(
    calendar.SUNDAY)

print(fecha.prmonth (2022, 11))