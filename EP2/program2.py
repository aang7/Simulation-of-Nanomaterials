#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import subprocess
import pygame

from math import sqrt


#clase 
class Particle:
    #"constructor"
    def __init__(self, (x, y), size): 
        self.x = x
        self.y = y
        self.size = size
        self.colour = (random.randint(0, 255), random.randint(0, 255), 255)
        self.thickness = 0

    def display(self):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.size, self.thickness)


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
    #print(sqrt(sum([x**2 for x in p])))
    abrir.write(str(sqrt(sum([x**2 for x in p]))) + "\n") #Escribiendo en archivo

#cmd = ['Rscript', '--vanilla','readLine.R', filename]

#ahora a ejecutar R script
#retcode = subprocess.call(cmd)

    
background_colour = (255,255,255)
(width, height) = (800, 700)

screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption('Trying to move particles')
screen.fill(background_colour)

x = 0
y = 0
repeticiones = 5
puntos_list = list()
xHalf = width/2
yHalf = height/2



running = True
switch = True

while running:
    #screen.fill(background_colour)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

            
    puntos_list = []
    
    for i in range(repeticiones):
        size = width * (random.randint(10, 11)/1000.0)    
        if (random.random() <= 0.5):
            if switch:
                x =random.randint(0 , int(width - size))
                y =random.randint(0, int(height - size))
                switch = False
            else:
                x =random.randint(0, int(width - size))
                y =random.randint(0, int(height - size))
                switch = True

            puntos_list.append(Particle((x , y ), int(size)))  
    #drawing particles
    for particle in puntos_list:
        particle.display()
        
        
    pygame.display.flip()
    

pygame.quit()
    
