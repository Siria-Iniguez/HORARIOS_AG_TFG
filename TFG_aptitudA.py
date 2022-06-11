#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 19:02:11 2022

@author: cati
"""



import random as rnd


#CREACION MATRIZ C 



EXAMENES = 180 
HORAS = 21

C = [0 for i in range(0,EXAMENES)]

with open("yor-f-83-3.stu") as dataset:
    for linea in dataset:
        LINEA = linea.split(" ")
        for j in range(0,len(LINEA)-1):
            C[int(LINEA[j]) - 1] +=1
            
print(C)


#EXAMENES DE CADA ALUMNOS 

ALUMNOS_ASIGNATURAS = [] 
#[[asignatura del alumno 0], [asignaturas del alumno 1],.......]


with open("yor-f-83-3.stu") as dataset:
    for linea in dataset:
        numero = "" 
        alumno =[]
        for j in linea  :
            if j in ["1","2","3","4","5","6","7","8","9","0"] :
                numero += j
            else:
                if (j != '\n'):
                    alumno.append(int(numero))
                numero =""
        ALUMNOS_ASIGNATURAS.append(alumno)

#CONSTRUIR UNA SOLUCION CUALQUIERA 

def vectorE (examenes,horas):
    horasexamenes = [ rnd.randint(1,horas)for i in range(0,examenes)]
    return horasexamenes



#FUNCION OBJETIVO 

#APTITUD DE UN ALUMNO

#todas las combinaciones posibles 
def aptitud_Alumno1(v,alumno):
    a = 0 
    for i in range(0,len(alumno)-1):
        distancia = abs (v[alumno[i]] - v[alumno[i+1]])
        if distancia == 0:
            a += 16
        if distancia == 1:
            a += 8
        if distancia == 2:
            a += 4
        if distancia == 3:
            a += 2
        if distancia == 4:
            a += 1
    return a 


def aptitud_Alumnos1 (v,alumnos):
    a = 0 
    for i in range (0,len(alumnos)):
        a += aptitud_Alumno1(v, alumnos[i])
    return a 


def el_Mejor(poblacion,alumnos):
    mejor = poblacion[0]
    for i in range(1,len(poblacion)):
        if aptitud_Alumnos1(poblacion[i],alumnos) < aptitud_Alumnos1(poblacion[i-1],alumnos):
            mejor = poblacion[i]
    return mejor 


#FACTIBILIDAD 

def factibleAlumno (v,alumno):
    apto = True 
    i = 0
    while apto == True and i < len(alumno):
        apto2 = True
        j = i 
        while apto2 == True and j < len(alumno):
            distancia = abs (v[alumno[i]] - v[alumno[j]])
            if distancia == 0 :
                apto2 = False 
            j += 1
        
        apto = apto2 
        i += 1
    return apto

def factibilidad (v,alumnos):
    apto = True 
    i = 0 
    while apto == True and i < len(alumnos):
        apto = factibleAlumno(v, alumnos[i])
        i += 1
    return apto


#SELECCION DE PADRES 

def seleccionPadres(poblacion,alumnos, k = 2):
    padres = []
    n = 0 
    while n < len(poblacion):
        a = rnd.randint(0,len(poblacion)-1)
        candidatoPadre = poblacion[a]
        adaptacion = aptitud_Alumnos1(candidatoPadre, alumnos)
        for j in range (0,k-1):
            c = rnd.randint(0,len(poblacion)-1)
            candidatoPadresig = poblacion[c]
            adaptacionsig = aptitud_Alumnos1(candidatoPadresig, alumnos)
            if adaptacionsig < adaptacion:
                candidatoPadre = candidatoPadresig
                adaptacion = adaptacionsig
        padres.append(candidatoPadre)
        n +=1
    return padres 
    
#CRUCE:

#listaN lista ordenada de indices primero empiezo con -1 y acabo con la longitud de padre1  
def cruce (padre1, padre2, listaN):
    padre1aux  = padre1
    padre2aux = padre2
    hijo1 = []
    hijo2 = []
    N = 0 
    i = 0 
    while i < len(listaN) - 1:
        if N%2 == 0 :
            hijo1 += padre1aux[listaN[i]+1: listaN[i+1]+1]
            hijo2 += padre2aux[listaN[i]+1: listaN[i+1]+1]
        else:
            hijo1 += padre2aux[listaN[i]+1: listaN[i+1]+1]
            hijo2 += padre1aux[listaN[i]+1: listaN[i+1]+1]
        N +=1
        i += 1
    return hijo1,hijo2
            
        


#HIJOS 
def crearlista (N):
    lista = [-1]
    for i in range (0,N):
        a = rnd.randint(1, EXAMENES)
        lista.append(a)
    lista.append(EXAMENES)
    lista.sort()
    lista.append(EXAMENES)
    return lista
        

def hijos(padres):
    hijos = []
    n = 0
    m = 1
    while n < len(padres) and m <len(padres):
        padre1 = padres[n]
        padre2 = padres[m]
        N = rnd.randint(1, EXAMENES)
        lista = crearlista(N)
        hijosCruce = cruce(padre1,padre2,lista)
        hijos.append(hijosCruce[0])
        hijos.append(hijosCruce[1])
        n += 2
        m +=2                
    return hijos  

#MUTACIÓN
def mutacion(horario,PM):
    for i in range (0,len(horario)):
        p = rnd.uniform(0, 1)
        if p < PM:
            a = rnd.randint(1, HORAS)
            horario[i] = a
    return horario 

#POBLACION 

def Population(tamano):
    poblacion = []
    for j in range (0,tamano):
        poblacion.append(vectorE(EXAMENES,HORAS))
    return poblacion 

#ELITISMO:
def recombiar_Elitismo(poblacion,hijos,alumnos):
    #print(longitud(hijos))
    total = poblacion + hijos
    mejor = el_Mejor(total,alumnos)
    nueva_generacion = [mejor]
    total.remove(mejor)
    n = len(nueva_generacion)
    while(n <= len(poblacion)):
        a = rnd.randint(0,len(total)-1)
        candidatoNuevaG = total[a]
        if factibilidad(candidatoNuevaG,alumnos):
            Pg = rnd.uniform(0, 1)
            if(Pg >= 0.2):
                nueva_generacion.append(total[a])
                total.remove(total[a])
                print(nueva_generacion)
                #print("")
                #print(longitud(nueva_generacion))
                n +=1
        else:
            Pg = rnd.uniform(0, 1)
            if(Pg < 0.2):
                nueva_generacion.append(total[a])
                print(nueva_generacion)
                total.remove(total[a] )       
                n +=1
    return nueva_generacion

def algoritmoGenetico(alumnos_asignaturas,tamano):  
    poblacion_inicial = Population(tamano)
    vueltas = 20
    while vueltas != 0 :
        l_padres = seleccionPadres(poblacion_inicial, alumnos_asignaturas, k=2)
        #print(longitud(l_padres))
        l_hijos = hijos(l_padres)
        #print(longitud(poblacion_inicial))
        #estoy en las ultimas vueltas 
        if (vueltas < 3 ):
            c = rnd.randint(0, tamano-1)
            Pm = rnd.uniform(0, 0.5)
            mutacion(poblacion_inicial[c],Pm)
        else: 
            c = rnd.randint(0, tamano-1)
            Pm = rnd.uniform(0, 0.5)
            mutacion(poblacion_inicial[c],Pm)
        poblacion_inicial = recombiar_Elitismo(poblacion_inicial,l_hijos,alumnos_asignaturas)
        vueltas -= 1
    mejor = el_Mejor(poblacion_inicial,alumnos_asignaturas)
    return mejor


         
mejores = algoritmoGenetico(ALUMNOS_ASIGNATURAS,8 )

print("mi horario")
print(mejores)

