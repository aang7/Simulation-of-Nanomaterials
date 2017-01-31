#! /usr/bin/Rscript
#Recibiendo argumentos
myArgs <- commandArgs(trailingOnly = TRUE)
fileName <- myArgs

data <- c(); #vector vacío
conn <- file(fileName,open="r") #Abriendo archivo

linn <-readLines(conn) #Leyend líneas del file 

for (i in 1:length(linn))
  data <- c(data, linn[i]) #Almacenando lineas en vector data

close(conn) #cerrando conexión
png("prueba.png")
barplot(as.numeric(data)) 
graphics.off();
#tal vez en viceversa funcione.
  
