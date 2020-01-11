#Edgar Vallejo Curti
#Calculadora lógica
#1 de octubre de 2019

import pylogical
from os import system

menu = 1 #Variable para repetir programa
variablesLista = []  # Lista de variables definidas
posibilidades = 0 #Número de casos, dependiendo de número de variables
nVariables = 0 #Número de variables
estadosLogicosLista = [] #Estados logicos, dependiendo del número de variables
ecuacionConEstados = []

while(menu):
    #Leer ecuación
    ecuacionOriginal = input("Ingresa una ecuación:\t")

    #Recuperar variables
    variablesLista = pylogical.rescateDeVariables(ecuacionOriginal) #Recuperar variables de string
    nVariables = len(variablesLista) #Saber cuantas variables son
    posibilidades = 2 ** (nVariables)  # 2 a la n posibilidades

    pylogical.printLista(variablesLista)
    print("")

    #Empezar a jugar con las posibilidades
    for repeticion in range(posibilidades):
        print(repeticion, end="\t")
        estadosLogicosLista = pylogical.definicionDeEstados(variablesLista, repeticion)
        pylogical.printLista(estadosLogicosLista)
        print("|", end = "\t")

        #Mapear los estados en la ecuación
        ecuacionConEstados = pylogical.mapearEcuacion(ecuacionOriginal,variablesLista,estadosLogicosLista)
        pylogical.printLista(ecuacionConEstados)

        print("|", end = "\t")
        #resolver ecuacion
        pylogical.printLista(pylogical.resolverEcuacion(ecuacionConEstados))



        print("")


    menu = int(input("Ingrese 0 si quieres dejar de correr el programa: "))
