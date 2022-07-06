#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 18:59:27 2022

@author: cati
"""

import TFG_AG as tfg


print("\033[0;30m")


def lecturaMV (dataset, forma, tamano, vueltas, examenes, horas, tiempo, alumnos, datasal):    
    MATRIZ_C = tfg.matrizC (tfg.lectura (dataset, forma, examenes, horas, alumnos)[0])
    VECTOR = [ -1 for i in range (0,examenes) ]    
    with open (datasal) as data:
        for linea in data:
            if len (linea)>0:
                LINEA = list (filter (lambda x : x != "", linea.split("\n")[0].split(" ")))               
                VECTOR[int(LINEA[0])-1] = int(LINEA[1])
    mejorS = tfg.funcionObj (VECTOR, MATRIZ_C, alumnos)     
    print("  El valor de la función objetivo para el conjunto ")
    print("  de datos " + str(datasal) + " es " + str(mejorS) )
    mejorAG = tfg.funcionObj (tfg.algoritmoGeneticoV (MATRIZ_C, None, 1, tamano, vueltas, 2, examenes, horas, alumnos, False)[0], MATRIZ_C, alumnos) 
    print("")
    print("  ALGORITMO GENÉTICO V:")
    print("   El mejor horario encontrado para " + str(dataset))
    print("   con el algoritmo algoritmoGeneticoV (..)")
    print("   para tamaño igual a " + str(tamano) + " y " + str(vueltas) + " vueltas")
    print("   tiene una función objetivo igual a " + str(mejorAG))    
    mejorAT = tfg.funcionObj (tfg.algoritmoGeneticoT (MATRIZ_C, None, 1, tamano, tiempo, 2, examenes, horas, alumnos, False)[0], MATRIZ_C, alumnos)
    print("")
    print("  ALGORITMO GENÉTICO T:")
    print("   El mejor horario encontrado para " + str(dataset))
    print("   con el algoritmo algoritmoGeneticoT (..)")
    print("   para tamaño igual a " + str(tamano) + " y un tiempo de " +str(tiempo // 60) + " min")
    print("   tiene una función objetivo igual a " + str(mejorAT))    
    print("")
    print("  UNA VUELTA: " + str (tfg.funcionObj (tfg.algoritmoGeneticoV (MATRIZ_C, None, 1, 100, 1, 2, examenes, horas, alumnos, False)[0], MATRIZ_C, alumnos)))




#print("\033[0;30m")
#print("")
#print(" DATOS: YOR83")
#lecturaMV ('YorkMills83.stu', 2, 100, 200, 181, 21, 421, 941, 'yor83.sol.txt')


#print("\033[0;30m")
#print(" DATOS: CAR91")
#lecturaMV ('Carleton91.exm', 1, 150, 200, 682, 35, 901, 16925, 'car91.sol.txt')

#print("\033[0;30m")
#print("")
#print(" DATOS: CAR92")
#lecturaMV ('Carleton92.exm', 1, 125, 300, 543, 32, 841, 18419, 'car92.sol.txt')

#print("\033[0;30m")
#print("")
#print(" DATOS: TRE92")
#lecturaMV ('Trent92.exm', 1, 125, 190, 261, 23, 600, 4360, 'tre92.sol.txt')

#print("\033[0;30m")
#print("")
#print(" DATOS: UTA92")
#lecturaMV('TorontoAS92.exm', 1, 200, 300, 622, 35, 901, 21266, 'uta92.sol.txt')


