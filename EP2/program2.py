#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import subprocess
import pygame

from math import sqrt


particulas = list()
(width, height) = (800, 700)

p = 30 #cuantas divisiones tengo desde el origen hasta l
l = height  #Longitud maxima
paso = l / p #Paso
permitidos = [x * paso - l for x in range(2 * p + 1)] #Valores permitidos


for y in range(8): #8 particulas
    coordenadas = list() #reseteando lista
    for j in range(2): #dos puntos para cada cordenada
        coordenadas.append(random.choice(permitidos)) #Escogiendo puntos dentro de los permitidos
        
    particulas.append(coordenadas) #Añadiendo particulas

    
background_colour = (255,255,255)

#Setting up pygame screen
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption('Trying to move particles')
screen.fill(background_colour)

x = 0
y = 0
puntos_list = list()
xHalf = width/2
yHalf = height/2

size = 5
colour = (random.randint(0, 255), random.randint(0, 255), 255)
thickness = 0


clock = pygame.time.Clock()
running = True
switch = True
cambio = 10
while running:
    screen.fill(background_colour)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    for i in range(len(particulas)):
        switch = bool(random.getrandbits(1)) #Faster than random.choice([True, False])
        xoy = random.randint(0, 1);
        if switch:
            particulas[i][xoy] += cambio
        else:
            particulas[i][xoy] -= cambio

        if particulas[i][xoy] < 0:
            particulas[i][xoy] += l
        elif particulas[i][xoy] > l:
            particulas[i][xoy] -= l

    for x in particulas:
        pygame.draw.circle(screen, colour, tuple([int(e) for e in x]), size, thickness)

    
    pygame.display.flip()
    clock.tick(12)

pygame.quit()
    
