#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 03:00:30 2022

@author: cati
"""
import TFG_AG as tfg
import matplotlib.pyplot as plt




########################################################
########################################################
########################################################
########                                        ########
########                                        ########
########    OPTIMIZACIÓN MEDIANTE MÉTODOS       ########
########           BIOINSPIRADOS                ########
########      TRABAJO DE FIN DE GRAFO           ########
########             ESTUDIOS                   ########
########                                        ########
########                                        ########
########################################################
########################################################
########################################################


# -- ESTUDIO POR VUELTAS FIJAS -- #
    
def estudioF26 (dataset, forma, tipo, vueltas, examenes, horas, alumnos, x, y, datasal):
    VECTOR_C, EXAMENES, HORAS, ALUMNOS = tfg.lectura (dataset, forma, examenes, horas, alumnos)
    MATRIZ_C = tfg.matrizC (VECTOR_C)
    VECTOR_SOLUCION = tfg.lecturaS (datasal, examenes)
    mejorA = tfg.funcionObj (tfg.algoritmoGeneticoV (MATRIZ_C, VECTOR_C, tipo, 35, vueltas, 2, examenes, horas, alumnos, False)[0], MATRIZ_C, alumnos)
    mejorT = 35     
    for i in range (40, 166, 5):
        x.append (i)
        horario = tfg.funcionObj (tfg.algoritmoGeneticoV (MATRIZ_C, VECTOR_C, tipo, i, vueltas, 2, examenes, horas, alumnos, False)[0], MATRIZ_C, alumnos)
        if (horario < mejorA):
            mejorA = horario 
            mejorT = i 
        y.append (horario)
    fig, ax = plt.subplots()
    ax.scatter (x, y)
    plt.xlabel ("Tamaño")
    plt.ylabel ("Adaptación")
    plt.title ("Nº vueltas fijo (V = " + str(vueltas) + "), Tamaño variando")
    plt.show ()
    print("        El mejor horario encontrado es para una po-") 
    print("        blación de tamaño " + str(mejorT) + " con una adaptación")
    print("        de " + str(mejorA) + " dando " + str (vueltas) + " vueltas")
    print("")
    print(" En el conjunto de datos: " + datasal)
    print(' el coste de su mejor horarios es: ' + str(tfg.funcionObj (VECTOR_SOLUCION, MATRIZ_C, alumnos)))    
        

## FIGURA 26 ##

#FIGURA 26.a
#print("\033[0;30m")
#estudioF26 ('EdHEC92.exm', 1, 1, 150, 81, 18, 2823, [],[], 'EdHEC92.sol')
#FIGURA 26.b
#print("\033[0;30m")
#estudioF26 ('EdHEC92.exm', 1, 1, 100, 81, 18, 2823, [],[], 'EdHEC92.sol')




# -- ESTUDIO POR TAMAÑO FIJO -- #

def estudioF27 (dataset,forma, tipo, tamano, examenes, horas, alumnos, x, y, datasal): 
    VECTOR_C, EXAMENES, HORAS, ALUMNOS = tfg.lectura (dataset, forma, examenes, horas, alumnos)
    MATRIZ_C = tfg.matrizC (VECTOR_C)
    VECTOR_SOLUCION = tfg.lecturaS (datasal, examenes)
    mejorA = tfg.funcionObj (tfg.algoritmoGeneticoV (MATRIZ_C, VECTOR_C,tipo, tamano, 50, 2, examenes, horas, alumnos, False)[0], MATRIZ_C, alumnos)
    mejorV = 50
    for i in range (100, 701, 50): 
        x.append (i)
        horario = tfg.funcionObj (tfg.algoritmoGeneticoV (MATRIZ_C, VECTOR_C, tipo, tamano, i, 2, examenes, horas, alumnos, False)[0], MATRIZ_C, alumnos)
        print(i)
        if (horario < mejorA):
            mejorA = horario 
            mejorV = i    
        y.append (horario)
    fig, ax = plt.subplots ()
    ax.scatter (x, y)
    plt.xlabel ("Vueltas")
    plt.ylabel ("Adaptación")
    plt.title ("Tamaño fijo (T = " + str(tamano) + "), Vueltas variando")
    plt.show ()
    print("       El mejor horario encontrado para una pobla-") 
    print("       ción de tamaño " + str(tamano) + " tiene una adaptación")
    print("       de " + str(mejorA) + " conseguido con " + str (mejorV) + " vueltas")
    print("")
    print(" En el conjunto de datos:" + datasal)
    print(' el coste de su mejor horarios es:' + str(tfg.funcionObj (VECTOR_SOLUCION, MATRIZ_C, alumnos)))


## FIGURA 27 ##

            
#FIGURA 27.a
print("\033[0;30m")
#estudioF27 ('St.Andrews83.exm', 1, 1, 100, 139, 13, 611, [],[], 'St.Andrews83.sol')
#FIGURA 27.b
print("\033[0;30m")
#estudioF27 ('St.Andrews83.exm', 1, 1, 150, 139, 13, 611, [],[], 'St.Andrews83.sol')
#FIGURA 27.c
print("\033[0;30m")
#estudioF27 ('St.Andrews83.exm', 1, 2, 100, 139, 13, 611, [],[], 'St.Andrews83.sol')
#FIGURA 27.d
print("\033[0;30m")
#estudioF27 ('St.Andrews83.exm', 1, 2, 150, 139, 13, 611, [],[], 'St.Andrews83.sol')





# -- ESTUDIO POR TIEMPO -- #


def estudioF28 (dataset, forma, tipo, tamano, examenes, horas, alumnos, a, t, datasal):
    VECTOR_C, EXAMENES, HORAS, ALUMNOS = tfg.lectura (dataset, forma, examenes, horas, alumnos)
    MATRIZ_C = tfg.matrizC (VECTOR_C)
    VECTOR_SOLUCION = tfg.lecturaS (datasal, examenes)
    mejorA = tfg.funcionObj (tfg.algoritmoGeneticoT (MATRIZ_C, VECTOR_C, tipo, tamano, 60, 2, examenes, horas, alumnos, False)[0], MATRIZ_C, alumnos)
    mejorT = 60
    a.append (mejorA)
    t.append (60)
    for i in range (60, 901, 30):
        t.append(i)
        horario = tfg.funcionObj (tfg.algoritmoGeneticoT (MATRIZ_C,VECTOR_C, tipo, tamano, i, 2, examenes, horas, alumnos, False)[0], MATRIZ_C, alumnos)
        print(i)
        if horario < mejorA:
            mejorA = horario 
            mejorT = i   
        a.append (horario) 
    fig, ax = plt.subplots()
    plt.xlabel ("Tiempo")
    plt.ylabel ("Adaptación")
    plt.title (" Tamaño (T = " + str(tamano) + "), Tiempo variando ")
    plt.plot (t, a , 'b')
    plt.show ()
    print("         El mejor horario encontrado para una pobla-") 
    print("         ción de tamaño " + str(tamano) + " tiene una adaptación")
    print("         de " + str(mejorA) + " conseguido con " + str (mejorT // 60) + " min")
    print("")
    print(" En el conjunto de datos: " + datasal)
    print(' el coste de su mejor horarios es: ' + str(tfg.funcionObj (VECTOR_SOLUCION, MATRIZ_C, alumnos))) 


## FIGURA 28 ##


#FIGURA 28.a
#print("\033[0;30m")
#estudioF28 ('Carleton91.exm', 1, 1, 150, 682, 35, 16925, [], [], 'Carleton91.sol')
#FIGURA 28.b
#print("\033[0;30m")
#estudioF28 ('Carleton91.exm', 1, 1, 175, 682, 35, 16925, [], [], 'Carleton91.sol')




#################################
### ESTUDIO GENERAR POBLACIÓN ### 
#################################


def estudioF29 (dataset, forma, examenes, horas, alumnos, datasal, intentos, s1, s2, sol):
    VECTOR_C, EXAMENES, HORAS , ALUMNOS = tfg.lectura (dataset, forma, examenes, horas, alumnos)
    MATRIZ_C = tfg.matrizC (VECTOR_C)
    VECTOR_SOLUCION = tfg.lecturaS (datasal, EXAMENES)
    for i in range (1, intentos + 1):
        s1.append (tfg.funcionObj (tfg.vectorS1 (EXAMENES, HORAS), MATRIZ_C, alumnos))
        s2.append (tfg.funcionObj (tfg.vectorS2 (VECTOR_C, EXAMENES, HORAS), MATRIZ_C, alumnos))
        sol.append (tfg.funcionObj (VECTOR_SOLUCION, MATRIZ_C, alumnos))    
    fig, ax = plt.subplots()
    plt.xlabel ("Intentos")
    plt.ylabel ("Adaptación")
    plt.title ("Estudio Generar Población")
    plt.plot (s1, linestyle= '--',marker='s', color='b', label = "vectorS1()")
    plt.plot (s2, color='r', marker='o',label = "vectorS2()")
    plt.plot (sol,  color='g', label = "solución P")
    plt.legend ()
    plt.show ()


## FIGURA 29 ##

#estudioF29 ('TorontoE92.exm', 1, 184, 10, 2750, 'TorontoE92.sol',  35, [], [], [])



def estudioF30 (dataset, forma, algoritmo, tipo, tamano, vueltas, tiempo, k,  examenes, horas, alumnos, datasal):
    VECTOR_C, EXAMENES, HORAS, ALUMNOS = tfg.lectura (dataset, forma, examenes, horas, alumnos)
    MATRIZ_C = tfg.matrizC (VECTOR_C)
    VECTOR_SOLUCION = tfg.lecturaS (datasal, examenes)
    if (algoritmo == 1):
        y = tfg.algoritmoGeneticoV (MATRIZ_C, VECTOR_C, tipo, 100, 80, 2, examenes, horas, alumnos, True)[1]
        fig, ax = plt.subplots ()
        plt.xlabel ("Vueltas")
        plt.ylabel ("Adaptación")
        plt.plot (y, color='b')
        if (tipo == 1): 
            plt.title ("Evolución Población (Tipo 1)")
        if (tipo == 2):
            plt.title ("Evolución Población (Tipo 2)")
        plt.show ()
    if (algoritmo == 2):
        mejor, x, y = tfg.algoritmoGeneticoT (MATRIZ_C, VECTOR_C, tipo, tamano, tiempo, 2, examenes, horas, alumnos, True)
        fig, ax = plt.subplots ()
        plt.xlabel ("Tiempo")
        plt.ylabel ("Adaptación")
        plt.plot (x, y, color='b')
        if (tipo == 1): 
            plt.title ("Evolución Población (Tipo 1)")
        if (tipo == 2):
            plt.title ("Evolución Población (Tipo 2)")
        plt.show ()
    print("")
    print(" En el conjunto de datos: " + str(datasal))
    print(' el coste de su mejor horarios es:', tfg.funcionObj (VECTOR_SOLUCION, MATRIZ_C, alumnos))
    


## FIGURA 30 ##
estudioF30 ('TorontoE92.exm', 1, 2, 1, 100, None, 421, 2, 184, 10, 11793, 'TorontoE92.sol')
#FIGURA 30.a
#estudioF30 ('TorontoE92.exm', 1, 1, 1, 100, 80, None, 2, 184, 10, 11793, 'TorontoE92.sol' )
#FIGURA 30.b
#estudioF30 ('TorontoE92.exm', 1, 1, 2, 100, 80, None, 2, 184, 10, 11793, 'TorontoE92.sol')
#FIGURA 30.c
#estudioF30 ('TorontoE92.exm', 1, 2, 1, 100, None, 421, 2, 184, 10, 11793, 'TorontoE92.sol')
#FIGURA 30.d
#estudioF30 ('TorontoE92.exm', 1, 2, 2, 100, None, 421, 2, 184, 10, 11793, 'TorontoE92.sol')






# -- ESTUDIO POR SELECCIÓN DE PADRES -- #

def estudioF31 (dataset, forma, algo, tipo, tamano, vueltas, examenes, horas, alumnos, x, y, z, t):
    VECTOR_C, EXAMENES, HORAS, ALUMNOS = tfg.lectura (dataset, forma, examenes, horas, alumnos)
    MATRIZ_C = tfg.matrizC(VECTOR_C)
    if (algo == 1):
        for i in range (75, 326, 50):
            x.append (i)
            y.append (tfg.funcionObj (tfg.algoritmoGeneticoV (MATRIZ_C, VECTOR_C, tipo, i, vueltas, 2, examenes, horas, alumnos, False)[0], MATRIZ_C, alumnos))
            z.append (tfg.funcionObj (tfg.algoritmoGeneticoV (MATRIZ_C, VECTOR_C, tipo, i, vueltas, 4, examenes, horas, alumnos, False)[0], MATRIZ_C, alumnos))
            t.append (tfg.funcionObj (tfg.algoritmoGeneticoV (MATRIZ_C, VECTOR_C, tipo, i, vueltas, 6, examenes, horas, alumnos, False)[0], MATRIZ_C, alumnos))
    if (algo == 2): 
        for i in range (60, 901,60):
            x.append (i)
            y.append (tfg.funcionObj (tfg.algoritmoGeneticoT(MATRIZ_C, VECTOR_C, tipo, tamano, i, 2, examenes, horas, alumnos, False)[0], MATRIZ_C, alumnos))
            z.append (tfg.funcionObj (tfg.algoritmoGeneticoT(MATRIZ_C, VECTOR_C, tipo, tamano, i, 4, examenes, horas, alumnos, False)[0], MATRIZ_C, alumnos))
            t.append (tfg.funcionObj (tfg.algoritmoGeneticoT(MATRIZ_C, VECTOR_C, tipo, tamano, i, 6, examenes, horas, alumnos, False)[0], MATRIZ_C, alumnos))
    plt.scatter (x, y, c = "blue", linewidths = 2, marker = "s", edgecolor = "blue", s = 20)
    plt.scatter (x, z, c = "red", linewidths = 2, marker = "^", edgecolor = "red", s = 20)
    plt.scatter (x, t, c = "green", linewidths = 2, marker = "o", edgecolor = "green", s = 20)
    if (algo ==1):
        plt.xlabel ("Tamaño")
    else:
        plt.xlabel ("Tiempo")
    plt.ylabel ("Adaptación")
    plt.title ("Comparación según el tamaño del torneo")
    plt.legend (("k = 2", "k = 4", "k = 6"), loc="upper right")
    plt.show()        
            

## FIGURA31 ##

#FIGURA31.a
#estudioF31 ('Trent92.exm', 1, 1, 1, None, 150, 261, 23, 4360, [],[],[],[])
#FIGURA33.b
#estudioF31 ('Trent92.exm', 1, 1, 2, None, 150, 261, 23, 4360, [],[],[],[])

#FIGURA33.c
#estudioF31 ('Trent92.exm', 1, 2, 1, 90, None, 261, 23, 4360, [],[],[],[])
#FIGURA31.d
#estudioF31 ('Trent92.exm', 1, 2, 2, 90, None, 261, 23, 4360, [],[],[],[])



# -- ESTUDIO COMPARAR SOLUCIONES -- #



def estudioF32 (dataset, forma, tamano1, tamano2, tamano3, vueltas, examenes, horas, alumnos, y, sol, datasal):
    VECTOR_C, EXAMENES, HORAS, ALUMNOS = tfg.lectura (dataset, forma, examenes, horas, alumnos)
    MATRIZ_C = tfg.matrizC (VECTOR_C)
    VECTOR_SOLUCION = tfg.lecturaS (datasal, examenes)
    ADAPTACION_VECTOR_SOLUCION = tfg.funcionObj (VECTOR_SOLUCION, MATRIZ_C, alumnos)  
    
    # ALGORITMO = 1
    # TIPO = 1, TAMAÑO = 100
    for i in range (0, 4):
        y.append (tfg.funcionObj (tfg.algoritmoGeneticoV (MATRIZ_C, None, 1, tamano1, vueltas, 2, examenes, horas, alumnos, False)[0], MATRIZ_C, alumnos))
        sol.append (ADAPTACION_VECTOR_SOLUCION)   
    
    # ALGORITMO = 1
    # TIPO = 2, TAMAÑO = 100   
    for i in range (0, 4): 
        y.append (tfg.funcionObj (tfg.algoritmoGeneticoV (MATRIZ_C, VECTOR_C, 2, tamano1, vueltas, 2, examenes, horas, alumnos, False)[0], MATRIZ_C, alumnos))
        sol.append (ADAPTACION_VECTOR_SOLUCION)
    
    # ALGORITMO = 1
    # TIPO = 1, TAMAÑO = 125
    for i in range (0, 4):  
        y.append (tfg.funcionObj (tfg.algoritmoGeneticoV (MATRIZ_C, None, 1, tamano2, vueltas, 2, examenes, horas, alumnos, False)[0], MATRIZ_C, alumnos))
        sol.append (ADAPTACION_VECTOR_SOLUCION)
    
    # ALGORITMO = 1
    # TIPO = 2, TAMAÑO = 125    
    for i in range (0, 4): 
        y.append (tfg.funcionObj (tfg.algoritmoGeneticoV (MATRIZ_C, VECTOR_C, 2, tamano2, vueltas, 2, examenes, horas, alumnos, False)[0], MATRIZ_C, alumnos))
        sol.append (ADAPTACION_VECTOR_SOLUCION)
    
    # ALGORITMO = 2
    # TIPO = 1, TAMAÑO = 150 
    for i in range (180, 721, 60):
        y.append (tfg.funcionObj (tfg.algoritmoGeneticoT (MATRIZ_C, None, 1, tamano3, i, 2, examenes, horas, alumnos, False)[0], MATRIZ_C, alumnos))
        print(i)
        sol.append (ADAPTACION_VECTOR_SOLUCION)   
    fig, ax = plt.subplots ()
    plt.xlabel ("Pruebas")
    plt.ylabel ("Adaptación")
    plt.plot (y, marker='o', color ='b', label = "AG")
    plt.plot(sol, marker='s', color='r', label = "PILAR")
    plt.title ("Comparación de soluciones")
    plt.legend ()
    plt.show ()


## FIGURA 32 ##

"""
#FIGURA 32.a 
print("")
print( '3. EAR83' )
print("")
estudioF32 ('EarlHaig83.exm', 1, 100, 125, 150, 80, 190, 24, 1125, [], [], 'EarlHaig83.sol')

#FIGURA 32.b
print("")
print(' 5. KFU93' )
print("")
estudioF32 ('KingFahd93.exm', 1, 300, 325, 350, 145, 461, 20, 5349, [], [], 'KingFahd93.sol')

#FIGURA 32.c 
print("")
print(' 4. HEC92' )
print("")
estudioF32 ('EdHEC92.exm', 1, 125, 150, 175, 95, 81, 18, 2823, [], [], 'EdHEC92.sol')

#FIGURA 32.d 
print("")
print( '6. LSE91' )
print("")
estudioF32 ('LSE91.exm', 1, 125, 190, 200, 90, 381, 18, 2726, [], [], 'LSE91.sol')
"""





     
        
    
    

