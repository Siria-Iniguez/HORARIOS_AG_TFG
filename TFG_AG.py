#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 00:56:30 2022

@author: cati
"""


import random as rnd
import time 




########################################################
########################################################
########################################################
########                                        ########
########                                        ########
########    OPTIMIZACIÓN MEDIANTE MÉTODOS       ########
########           BIOINSPIRADOS                ########
########      TRABAJO DE FIN DE GRAFO           ########
########        ALGORITMOS GENÉTICOS            ########
########                                        ########
########                                        ########
########################################################
########################################################
########################################################



####################################
### CONJUNTO DE DATOS DE ENTRADA ###
####################################



# -- LECTURA DE DATOS DE ENTRADA PARA LAS DISTINTAS UNIVERSIDADES -- #


print( "CONJUNTOS DE DATOS DE ENTRADA PARA  EL PROBLEMA DE ASIGNACIÓN DE HORARIOS")
print("")

print( '1. CAR91' )
print( 'dataset = Carleton91.exm, datasal = Carleton91.sol')
print( 'EXAMENES = 682, HORAS = 35, ALUMNOS = 16925')
print("")


print( '2. CAR92' )
print( 'dataset = Carleton92.exm, datasal = Carleton92.sol')
print( 'EXAMENES = 543, HORAS = 32, ALUMNOS = 18419')
print("")


print( '3. EAR83' )
print( 'dataset = EarlHaig83.exm, datasal = EarlHaig83.sol')
print( 'EXAMENES = 190, HORAS = 24', 'ALUMNOS = 1125')
print("")


print( '4. HEC92' )
print( 'dataset = EdHEC92.exm, datasal = EdHEC92.sol')
print( 'EXAMENES = 81, HORAS = 18, ALUMNOS = 2823')
print("")


print( '5. KFU93' )
print( 'dataset = KingFahd93.exm, datasal = KingFahd93.sol')
print( 'EXAMENES = 461, HORAS = 20, ALUMNOS = 5349')
print("")


print( '6. LSE91' )
print(' dataset = LSE91.exm, datasal = LSE91.sol')
print( 'EXAMENES = 381, HORAS = 18, ALUMNOS = 2726')
print("")

print( '7.STA83')
print('dataset = St.Andrews83.exm, datasal = St.Andrews83.sol')
print( 'EXAMENES = 139, HORAS = 13, ALUMNOS = 611')
print("")


print( '8. TRE92')
print( 'dataset = Trent92.exm, datasal = Trent92.sol')
print( 'EXAMENES = 261, HORAS = 23, ALUMNOS = 4360')
print("")

      
print( '9. UTA92' )
print( 'dataset = TorontoAS92.exm, datasal = TorontoAS92.sol')
print( 'EXAMENES = 622, HORAS = 35, ALUMNOS 21266')
print("")


print( '10. UTE92' )
print('dataset = TorontoE92.exm, datasal = TorontoE92.sol')
print( 'EXAMENES = 184, HORAS = 10, ALUMNOS = 2750' )
print("")


print( '11. YOR83' )
print( 'dataset = YorkMills83.stu, datasal = YorkMills83.sol ')
print( 'EXAMENES = 181, HORAS = 21, ALUMNOS = 941')
print("")




############################
### CREACIÓN DE MATRIZ C ###
############################



# -- CONSTRUIMOS  LA DIAGONAL DE LA MATRIZ C -- #

#Construimos la diagonal de la matriz C con los datos proporcionados en el 
#conjunto de datos marcado

#print("")
#print ("LEYENDA:")
#print("__FORMA__ ¿formato de los datos de entrada? ")
#print("FORMA 1: modo .exm" )
#print("FORMA 2: modo .stu" )

def lectura (dataset, forma, examenes, horas, alumnos) :
    VECTOR_C = [0 for i in range (0,examenes)]
    try:
        if forma == 2:
            with open(dataset) as data:
                for linea in data:
                    LINEA = list (filter (lambda x : x != "", linea.split("\n")[0].split(" ")))
                    VECTOR_C[ int(LINEA[1] ) - 1] += 1
        elif forma == 1: 
            with open(dataset) as data:
                i = 0
                for linea in data:
                    LINEA = list (filter (lambda numero: numero != "", linea.split("\n")[0].split(" ")))         
                    if (len(LINEA) >= 2):    
                            VECTOR_C[i] = int( LINEA[1] ) 
                    i += 1
    except:
        print('INTRODUCISTE MAL ALGÚN DATO')
    return VECTOR_C, examenes, horas, alumnos


# -- CONSTRUIR TOTAL DE LA PARTE SUPERIOR DE LA MATRIZ C DE LOS APUNTES -- # 

def matrizC (vectorC):
    MATRIZ_C = vectorC 
    for i in range (0, len(vectorC) - 1):
        MATRIZ_C[i] = [MATRIZ_C[i]]
        for j in range (i + 1, len(vectorC)):
            MATRIZ_C[i].append (MATRIZ_C[i][0] + MATRIZ_C[j])
    MATRIZ_C[len(vectorC) - 1] = [MATRIZ_C[len(vectorC) - 1 ]]         
    return MATRIZ_C




# -- CONSTRUIR UNA SOLUCIÓN CUALQUIERA DE FORMA ALEATORIA -- #

#print("")
#print ("LEYENDA:")
#print("__TIPO__ ¿formato de los datos de entrada? ")
#print("TIPO 1: función vectorS (..)" )
#print("TIPO 2: función vectorS2 (..)" )

def vectorS1 (examenes, horas):
    horasexam = [ rnd.randint(0, horas - 1) for i in range(0, examenes) ]
    return horasexam


# -- CREAR HORARIO QUE ESTÉ "BIEN" HECHO DESDE EL PRINCIPIO -- #


def vectorS2 (vector, examenes, horas):
    matrizaux = vector.copy() 
    horasexam = [-1 for i in range (0, examenes)]
    i = rnd.randint (0, horas - 1)
    j = (i + 6) % horas 
    N = 0
    while (len(matrizaux) > 0) :
        if (N % 2 == 0):
            maximo = max (matrizaux)
            horasexam[vector.index (maximo)] = i 
            matrizaux.remove (maximo)
            i = (i + 1) % (horas)
        else: 
            maximo = max (matrizaux)
            horasexam[vector.index (maximo)] = j 
            matrizaux.remove (maximo)
            j = (j + 1) % (horas)
        N = (N + 1) % 2
    return horasexam


#########################
### FUNCIÓN OBJETIVO ### 
#########################



# -- APTITUD DE UN HORARIO SEGUN LA FORMULA DE LOS APUNTES -- #

def funcionObj (horario, matriz, alumnos):
    a = 0 
    for i in range (len (matriz)):
        for j in range (i + 1, len (matriz[i])):
            distancia = abs (horario[i] - horario[j])
            Alumnos = matriz[i][j]
            if distancia == 1:
                a += 16 * Alumnos
            if distancia == 2:
                a += 8 * Alumnos
            if distancia == 3:
                a += 4 * Alumnos
            if distancia == 4:
                a += 2 * Alumnos
            if distancia == 5:
                a += 1 * Alumnos 
    return round (a / alumnos, 2)


# -- APTITUD DE UN HORARIO PENALIZANDO LA INFACTIBILIDAD -- #

def funcionObj2 (horario, matriz, alumnos):
    a = 0 
    for i in range (len(matriz)):
        for j in range (i + 1, len(matriz[i])):
            distancia = abs(horario[i] - horario[j])
            Alumnos = matriz[i][j]
            if distancia == 1:
                a += 16 * Alumnos
            if distancia == 2:
                a += 8 * Alumnos
            if distancia == 3:
                a += 4 * Alumnos
            if distancia == 4:
                a += 2 * Alumnos
            if distancia == 5:
                a += 1 * Alumnos 
            if distancia == 0:
                a += 64 * Alumnos
    return round (a / alumnos, 2)




####################
### FACTIBILIDAD ###
####################

# -- FORMA UNO DE COMPROBAR LA FACTIBILIDAD DE UN HORARIO -- #
  
def factibilidad (horario, matriz):
    a = 0 
    i = 0 
    while (i < len(matriz) and a == 0):
        j = i + 1
        while (j < len(matriz[i]) and a == 0):
            if horario[i] == horario[j]:
                a +=  matriz[i][j] 
            j += 1
        i += 1
    return a == 0 




##############################
### CALCULO DE LOS MEJORES ###
##############################



# -- DEFINICION DEL MEJOR ENTRE DOS HORARIOS -- #

def mejorF (horario1, horario2, matriz, alumnos):
    if factibilidad (horario1,matriz) and not factibilidad (horario2,matriz): 
        return horario1 
    else:
        if factibilidad (horario2,matriz) and not factibilidad (horario1,matriz):
            return horario2 
        else:
            if funcionObj (horario1, matriz, alumnos) < funcionObj (horario2, matriz, alumnos):
                return horario1
            else:
                return horario2


# -- MEJOR HORARIO DE LA POBLACION -- # 
            
def el_MejorP (poblacion, matriz, alumnos):
    mejor = poblacion[0]
    for i in range (1, len(poblacion)):
        mejor = mejorF (poblacion[i], mejor, matriz, alumnos)
    return mejor 




###########################
### SELECCION DE PADRES ### 
###########################



# -- SELECCIÓN POR TORNEO DETERMINISTICO -- ##

def seleccionPadres (poblacion, matriz, k, alumnos):
    padres = []
    n = 0 
    while n < len(poblacion):
        a = rnd.randint (0, len(poblacion) - 1)
        candidatoPadre = poblacion[a]
        for j in range (1, k):
            c = rnd.randint (0, len(poblacion) - 1)
            candidatoPadresig = poblacion[c]
            candidatoPadre = mejorF (candidatoPadre, candidatoPadresig, matriz, alumnos)
        padres.append (candidatoPadre)
        n += 1
    return padres 




#############
### CRUCE ###
#############



# -- CRUCE POR N PUNTOS -- #
# PARAMETRO: listaN #
# L = [0,...,N+1] | L[0] = -1 and L[N+1] = len(padre1) and L[i] < L[j] para todo 1 <= i < j <=  N 

def cruceN (padre1, padre2, listaN):
    padre1aux  = padre1.copy()
    padre2aux = padre2.copy()
    hijo1 = []
    hijo2 = []
    N = 0 
    i = 0 
    while i < len(listaN) - 1:
        if N%2 == 0 :
            hijo1 += padre1aux[listaN[i] + 1: listaN[i+1] + 1]
            hijo2 += padre2aux[listaN[i] + 1: listaN[i+1] + 1]
        else:
            hijo1 += padre2aux[listaN[i] + 1: listaN[i+1] + 1]
            hijo2 += padre1aux[listaN[i] + 1: listaN[i+1] + 1]
        N += 1
        i += 1
    return hijo1,hijo2

## -- CRUCE UNIFORME -- ##

def cruceU (padre1, padre2, PM):
    padre1aux  = padre1.copy()
    padre2aux = padre2.copy()
    hijo1 = []
    hijo2 = []
    for i in range (0, len(padre1)):
        pm = rnd.uniform(0, 1)
        if pm < PM:
            hijo1.append (padre1aux[i])
            hijo2.append (padre2aux[i])
        else: 
             hijo1.append (padre2aux[i])
             hijo2.append (padre1aux[i])
    return hijo1, hijo2




#############
### HIJOS ###
#############

# -- LISTA ORDENADA -- ##


# N <= EXAMENES - 1 
def crearLista (N, examenes):
    lista = [-1] + rnd.sample (range (0, examenes - 1), N)
    lista.sort()
    lista.append (examenes)
    return lista

def hijos (padres, examenes):
    hijos = []
    n = 0
    m = 1
    while n < len(padres) and m < len(padres):
        padre1 = padres[n]
        padre2 = padres[m]
        N = rnd.randint (1, examenes // 2)
        lista = crearLista (N, examenes)
        hijosCruce = cruceN (padre1, padre2, lista)
        hijos.append (hijosCruce[0])
        hijos.append (hijosCruce[1])
        n += 2
        m += 2                
    return hijos




################
### MUTACIÓN ###
################

def mutacion (calen, PM, horas):
    for i in range (0, len(calen)):
        p = rnd.uniform (0, 1)
        if p < PM:
            a = rnd.randint (0, horas - 1)
            calen[i] = a
    return calen 




#################
### POBLACIÓN ###
#################

def population (tamano, vector, tipo, examenes, horas):
    poblacion = []
    if tipo == 1:
        for j in range (0, tamano):
            poblacion.append (vectorS1 (examenes, horas) )
    if tipo == 2:
        for j in range (0, tamano):
            poblacion.append(vectorS2 (vector, examenes, horas))        
    return poblacion 




####################################
### REMPLAZAMIENTO GENERACIONAL ###
###################################

# -- ELITISMO -- #
def recombiar_Elitismo (poblacion, hijos, matriz, alumnos):
    total = poblacion + hijos
    mejor = el_MejorP (total, matriz, alumnos)
    nueva_generacion = [mejor]
    total.remove (mejor)
    n = len(nueva_generacion)
    while  n <= len(poblacion) :
        a = rnd.randint (0, len(total) - 1)
        candidatoNuevaG = total[a]
        if factibilidad (candidatoNuevaG, matriz):
            nueva_generacion.append (total[a])
            total.remove (total[a])
            n += 1
        else: 
            Pg = rnd.uniform (0, 1)
            if (Pg < 0.5):
                nueva_generacion.append (total[a])
                total.remove (total[a])       
                n += 1
    return nueva_generacion




###################################
### ALGORITMO GENÉTICO VUELTAS ###
##################################

def algoritmoGeneticoV (matriz, vector, tipo, tamano, vueltas, k, examenes, horas, alumnos, necesito):  
    poblacion_inicial = population (tamano, vector, tipo, examenes, horas)
    Vueltas = vueltas 
    ultimas = vueltas // 8
    mejores = []
    while Vueltas != 0 :
        l_padres = seleccionPadres (poblacion_inicial, matriz, k, alumnos)
        l_hijos = hijos (l_padres, examenes)
        #estoy en las ultimas vueltas 
        if (Vueltas < ultimas):
            Pm = rnd.uniform (0, 0.02)
            for i in range (0, examenes // 32):
                c = rnd.randint (0, tamano - 1)
                mutacion (poblacion_inicial[c], Pm, horas)
                
        else: 
            Pm = rnd.uniform (0.1, 0.5)
            for i in range (0, examenes // 16):
                c = rnd.randint (0, tamano - 1)
                mutacion (poblacion_inicial[c], Pm, horas)                
        poblacion_inicial = recombiar_Elitismo (poblacion_inicial, l_hijos, matriz, alumnos)
        if necesito == True:
            mejores.append (funcionObj (poblacion_inicial[0], matriz, alumnos))
        Vueltas -= 1
    mejor = poblacion_inicial[0]
    return mejor, mejores


##################################
### ALGORITMO GENÉTICO TIEMPO ###
#################################

def algoritmoGeneticoT (matriz, vector, tipo, tamano, tiempo, k, examenes, horas, alumnos, necesito):
    poblacion_inicial = population(tamano, vector, tipo, examenes, horas)
    start = time.time ()
    TIEMPO = 0
    mejores = []
    listaT = [] 
    while TIEMPO < tiempo :
        l_padres = seleccionPadres (poblacion_inicial, matriz, k, alumnos)
        l_hijos = hijos (l_padres, examenes)
        #estoy en las ultimas vueltas 
        if TIEMPO < 60 :
            Pm = rnd.uniform (0, 0.03)
            for i in range (0, examenes // 32):
                c = rnd.randint (0, tamano - 1)
                mutacion (poblacion_inicial[c], Pm, horas)
        else: 
            Pm = rnd.uniform (0.1, 0.5)
            for i in range (0, examenes // 16):
                c = rnd.randint(0, tamano - 1)
                mutacion (poblacion_inicial[c], Pm, horas)
        poblacion_inicial = recombiar_Elitismo (poblacion_inicial, l_hijos, matriz, alumnos)
        fin = time.time ()
        TIEMPO = abs (fin - start)
        if necesito == True :
            mejores.append (funcionObj (poblacion_inicial[0], matriz, alumnos))
            listaT.append (TIEMPO)
    mejor = poblacion_inicial[0]
    return mejor, listaT, mejores




##################################
### LECTURA DE DATOS DE SALIDA ###
##################################

# -- OJO cuidado el examen 3 esta en la posicion 2 -- #

def lecturaS (datasal, examenes):
    vectorSol = [0 for i in range (0, examenes)]
    with open (datasal) as data:
        for linea in data:
            LINEA = linea.split("\t")
            if len(LINEA) >= 2:
                vectorSol[int (LINEA[0]) - 1] = int( LINEA[1] )
    return vectorSol

    