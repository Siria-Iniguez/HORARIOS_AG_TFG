#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 20:32:41 2022

@author: cati
"""



import random as rnd


EXAMENES = 180 

HORAS = 21

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
      

#print("CADA ALUMNO CON SUS ASIGNATURAS")        
#print(ALUMNOS_ASIGNATURAS)

def horario_horas(horas):
    horario = []
    for i in range (0,horas):
        horario.append([])
    return horario
        
def horario(examenes, horas):
    horario = horario_horas(horas)
    n_examenes = examenes 
    n = 0 
    examenes_ya_cogidos = [-1]
    while n_examenes != 0:
        examen = rnd.randint(0,examenes-1)
        while examen in examenes_ya_cogidos:
            examen = rnd.randint(0,examenes)
        examenes_ya_cogidos.append(examen)
        horario[n].append(examen)
        n_examenes -= 1 
        n = (n+ 1)%horas
    return horario

"""
horario1 = horario(EXAMENES,HORAS)
print("horario Prueba")
print(horario1)        
"""     

      

def aptitudAlumno(alumno,horario):
    valido = True 
    adaptacion = 0 
    n = 0 
    ALUMNO = alumno 
    while n < len(horario) and len(ALUMNO)>0: 
        inicio = 0 
        
        j = 0 
        while (j<len(ALUMNO)):
            if ALUMNO[j] in horario[n]:
                inicio +=1
                ALUMNO.remove(ALUMNO[j])
                j -=1
            j +=1
        if inicio > 0:      
            pasos = 0
            cambio = False
            while pasos < 5 and n <len(horario) and cambio == False :
                n +=1
                for i in range (0,len(ALUMNO)):
                    if n <len(horario) and  ALUMNO[i] in horario[n] :
                        if pasos == 0:
                            adaptacion += inicio*16
                        if pasos == 1:
                            adaptacion += inicio*8
                        if pasos == 2:
                            adaptacion += inicio*4
                        if pasos == 3:
                            adaptacion += inicio*2
                        cambio = True 
                pasos +=1
        else: 
            n +=1
        valido = valido and (inicio<=1)
    return valido,adaptacion


                    
def aptitudAlumnos(alumnos,horario):
    valido = True 
    adaptacion = 0 
    for i in range(0,len(alumnos)):
        v,a = aptitudAlumno(alumnos[i],horario)
        valido = valido and v
        adaptacion +=  a
    return valido, adaptacion


def seleccionPadres(poblacion,alumnos, k = 2):
    padres = []
    n = 0 
    while n < len(poblacion):
        a = rnd.randint(0,len(poblacion)-1)
        candidatoPadre = poblacion[a]
        adaptacion = aptitudAlumnos(alumnos,candidatoPadre)[1]
        for j in range (0,k-1):
            c = rnd.randint(0,len(poblacion)-1)
            candidatoPadresig = poblacion[c]
            adaptacionsig = aptitudAlumnos(alumnos,candidatoPadresig)[1]
            if adaptacionsig < adaptacion:
                candidatoPadre = candidatoPadresig
                adaptacion = adaptacionsig
        padres.append(candidatoPadre)
        n +=1
    return padres            

 


#grupo se puede escoger de 1 a len(horario1)
def cruce1(horario1,horario2,grupos):
    N = 0 
    individuos = len(horario1) // grupos  
    horario1_aux = horario1
    horario2_aux = horario2
    hijo1 = []
    hijo2 = []
    indice = 0 
    while N < grupos:
        if N%2 == 0 :
            hijo1 += horario1_aux[indice:indice+individuos]
            hijo2 += horario2_aux[indice:indice+individuos]
        else:
            hijo1 += horario2_aux[indice:indice+individuos]
            hijo2 += horario1_aux[indice:indice+individuos]
        N +=1
        indice += individuos
    if indice < len(horario1):
        hijo1 += horario1_aux[indice:len(horario1)]
        hijo2 += horario2_aux[indice:len(horario1)]
            
    return hijo1,hijo2
           
#se reproducen los padres 

def hijos(padres):
    hijos = []
    n = 0
    m = 1
    while n < len(padres) and m <len(padres):
        padre1 = padres[n]
        padre2 = padres[m]
        a = rnd.randint(1, len(padre1))
        hijosCruce = cruce1(padre1,padre2,a)
        hijos.append(hijosCruce[0])
        hijos.append(hijosCruce[1])
        n += 2
        m +=2
                  
    return hijos     



#PREGUNTAR SI SOLO ES PARA LOS HIJOS Y TAMBIEN SI VALE SOLO COGER DOS PARA MUTAR 
def mutacion(horario):
    a = rnd.randint(0,21-1)
    b = rnd.randint(0,21-1)
    horario[a], horario[b] = horario[b],horario[a]
    return horario 


def Population(tamano):
    poblacion = []
    for j in range (0,tamano):
        poblacion.append(horario(EXAMENES,HORAS))
    return poblacion 


#hay que revisarlo 
def el_Mejor(poblacion,alumnos):
    mejor = poblacion[0]
    for i in range(1,len(poblacion)):
        if aptitudAlumnos(alumnos,poblacion[i])[1] < aptitudAlumnos(alumnos,poblacion[i-1])[1]:
            mejor = poblacion[i]
    return mejor 
         

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
        if aptitudAlumnos(alumnos,candidatoNuevaG)[0]:
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

"""
def longitud (poblacion):
    longitud = True 
    for j in range (0,len(poblacion)):
        longitud =longitud and len(poblacion[j])==21
    return longitud
"""

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
            Pm = rnd.uniform(0, 1)
            if Pm <0.2:
                c = rnd.randint(0, tamano-1)
                mutacion(poblacion_inicial[c])
        else: 
            Pm = rnd.uniform(0, 1)
            if Pm >=  0.2:
                c = rnd.randint(0, tamano-1)
                mutacion(poblacion_inicial[c])
                
        poblacion_inicial = recombiar_Elitismo(poblacion_inicial,l_hijos,alumnos_asignaturas)
        vueltas -= 1
    mejor = el_Mejor(poblacion_inicial,alumnos_asignaturas)
    return mejor


         
mejores = algoritmoGenetico(ALUMNOS_ASIGNATURAS,8 )

print("mi horario")
print(mejores)







