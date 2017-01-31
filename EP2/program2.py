#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import subprocess
from math import sqrt

particulas = list()

p = 30 #cuantas divisiones tengo desde el origen hasta l
l = 3.5 #Longitud maxima
paso = l / p #Paso
permitidos = [x * paso - l for x in range(2 * p + 1)] #Valores permitidos


for y in range(8): #8 particulas
    coordenadas = list() #reseteando lista
    for j in range(2): #dos puntos para cada cordenada
        coordenadas.append(random.choice(permitidos)) #Escogiendo puntos dentro de los permitidos
        
    particulas.append(coordenadas) #Añadiendo particulas

filename = 'salida.txt'
abrir = open(filename, "w")

#distancias eucladiana
for p in particulas:
    print(sqrt(sum([x**2 for x in p])))
    abrir.write(str(sqrt(sum([x**2 for x in p]))) + "\n") #Escribiendo en archivo

cmd = ['Rscript', '--vanilla','readLine.R', filename]

#ahora a ejecutar R script
retcode = subprocess.call(cmd)

#Aqui me quede--- todavia en versión pañales...
import random
x = 0
y = 0
repeticiones = 200
puntos_list = list()

for i in range(repeticiones):
    coordenadas = list()
    if (random.random() <= 0.5):
        x +=1
        y +=2
    else:
        x -=1
        y -=2
        
    coordenadas.append(x)
    coordenadas.append(y)
    puntos_list.append(coordenadas)


print puntos_list
