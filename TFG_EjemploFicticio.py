#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 14:21:22 2022

@author: cati
"""


import TFG_AG as tfg  

###############################
###############################
### TESTEO DE LAS FUNCIONES ###
###############################
###############################


#########################
### CREACION MATRIZ C ###
#########################

#EXAMENES = 5
#HORAS = 7 


print("\033[0;30m]")

VECTOR_C, EXAMENES, HORAS, ALUMNOS = tfg.lectura ('prueba.txt', 1, 5, 7, 10)

print("")
print (" EL VECTOR" + " C" +  " ES: ")
print ("", VECTOR_C)



MATRIZ_C = tfg.matrizC(VECTOR_C)
print("")
print(" LA MATRIZ MATRIZ_C ES: ")
print("", MATRIZ_C)



V1 = tfg.vectorS1 (EXAMENES, HORAS)
print("")
print(" GENERACIÓN HORARIO TIPO 1:")
print("", V1)
print("")
print(" FUNCIÓN OBJETIVO: ", tfg.funcionObj(V1, MATRIZ_C, ALUMNOS))
print(" FACTIBILIDAD: ", tfg.factibilidad(V1, MATRIZ_C))

V2 = tfg.vectorS2 (VECTOR_C, EXAMENES, HORAS)
print("")
print(" GENERACIÓN HORARIO TIPO 2:")
print("", V2)
print("")
print(" FUNCIÓN OBJETIVO: ", tfg.funcionObj(V2, MATRIZ_C, ALUMNOS))
print(" FACTIBILIDAD: ", tfg.factibilidad(V2, MATRIZ_C))


POBLACION = tfg.population (3, VECTOR_C, 1, EXAMENES, HORAS)
print("")
print (" GENERAMOS UNA POBLACIÓN: ")
print("", POBLACION)



PADRES = tfg.seleccionPadres (POBLACION, MATRIZ_C, 2, ALUMNOS)
print("")
print (" LOS PADRES SON: ")
print("", PADRES)


PADRE1 = PADRES[0]
PADRE2 = PADRES[1]


LISTA = tfg.crearLista (3, EXAMENES)
print("")
print(" PADRE 1:", PADRE1," PADRE 2:",PADRE2)
print("")
print(" LISTA_N:", LISTA)


HIJOS = tfg.cruceN (PADRE1, PADRE2, LISTA)
print("")
print(" HIJOS:")
print("", HIJOS)


print("")
print(" CRUCE UNIFORME PM = 0.2:")
HIJOS = tfg.cruceU (PADRE1, PADRE2, 0.2)
print(" HIJOS:", HIJOS)


print("")
print(" CRUCE UNIFORME PM = 0.8:")
HIJOS = tfg.cruceU (PADRE1, PADRE2, 0.8)
print(" HIJOS:", HIJOS)



V = [3, 6, 4, 0, 1]
W = [3, 6, 4, 0, 1]
print("")
print(" VECTOR QUE SERÁ MUTADO: ")
print("", V)


V_1 = tfg.mutacion (V, 0.2, HORAS)
print("")
print(" MUTACIÓN PARA PM = 0.2:")
print("", V_1)


V_2 = tfg.mutacion(W, 0.8, HORAS)
print("")
print(" MUTACIÓN PARA PM = 0.8:")
print("", V_2)












