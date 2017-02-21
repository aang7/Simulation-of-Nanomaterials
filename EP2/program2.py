#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import subprocess
import pygame

from math import sqrt

(width, height) = (800, 700)

p = 30 #cuantas divisiones tengo desde el origen hasta l
lx = width  #Longitud maxima en x
ly = height #Longitud maxima en y

#Sacar el minimo entre width y heigt para sacar valores iniciales
#despues sacar mi lx y ly para tener toda la pantalla como el rango maximo de valores
l = min(lx, ly)
paso = l / p #Paso
permitidos = [x * paso - l for x in range(2 * p + 1)] #Valores permitidos
    
background_colour = (255,255,255)

#Setting up pygame screen
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption('Trying to move particles')
screen.fill(background_colour)

puntos_list = list()
size = 5
colour = (random.randint(0, 255), random.randint(0, 255), 255)
thickness = 0
clock = pygame.time.Clock()
particlesQTY = 20 #cantidad de particulas
particulas = list()

def createParticles(lenx, listaPermitidos):
    particulas = list()
    for y in range(lenx): #cantidad particulas
        coordenadas = list() #reseteando lista
        for j in range(2): #dos puntos para cada cordenada
            coordenadas.append(random.choice(listaPermitidos)) 
        
        particulas.append(coordenadas) #Añadiendo particulas
    return particulas

def updateSetup(width, height):
    global lx, ly, l, permitidos, particulas, p, paso, particlesQTY
    lx = width
    ly = height
    l = min(lx, ly)
    paso = l / p
    permitidos = [x * paso - l for x in range(2 * p + 1)]
    particulas = createParticles(particlesQTY, permitidos)
   
particulas = createParticles(8, permitidos)

running = True
switch = True
cambio = 10

while running:
    screen.fill(background_colour)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            updateSetup(event.w, event.h)
    
    for i in range(len(particulas)):
        switch = bool(random.getrandbits(1)) #Faster than random.choice([True, False])
        xoy = random.randint(0, 1);
        if switch:
            particulas[i][xoy] += cambio
        else:
            particulas[i][xoy] -= cambio

        if xoy == 0:
            if particulas[i][xoy] < 0:
                particulas[i][xoy] += lx
            elif particulas[i][xoy] > lx:
                particulas[i][xoy] -= lx
        else:
            if particulas[i][xoy] < 0:
                particulas[i][xoy] += ly
            elif particulas[i][xoy] > ly:
                particulas[i][xoy] -= ly
            
    for x in particulas:
        pygame.draw.circle(screen, colour, tuple([int(e) for e in x]), size, thickness)

    
    pygame.display.flip()
    clock.tick(12)

pygame.quit()
    

