def rescateDeVariables(string):
    variables = [] #Variables a devolver
    simbolosDefinidos = ["(", ")", "~", "^", "v", "+", "-", "=", " "]

    for char in string:     #Para todo char en el string
        if simbolosDefinidos.count(char) == 0:   #Si el char no es un simbolo definido
            if variables.count(char) == 0:      #Si el char no está en la lista deifnida
                variables.append(char)          #Agregar a lista de variables

    variables.sort() #Acomodar variables, solo por comodidad
    return variables

def parOImparBinario(number, exp):
    n = int(number / 2**exp)
    #Esta funcion devuelve valores logicos
    #Si n / el exp es par, tendrá que ser falso
    if n % 2  == 0:
        return False
    else:
        return True

def definicionDeEstados(variables, repeticion):
    #Variables como lista
    #Repeticion = repeticion binaria en la que va
    nVariable = 0 #Indica que variable es

    estadoBinarioLista = [] #Estados a devolver
    for index in range(len(variables)):
        nVariable = len(variables) - index - 1
        estadoBinarioLista.append(parOImparBinario(repeticion, nVariable))
        #Agrega a la lista de estados un estado, dependiendo de la posición y la repeticion

    return estadoBinarioLista

def printLista(lista):
    for index in range(len(lista)):
        print(lista[index], end="\t")

def negacionLogico(listaEntrada):
    listaSalida = [] #Lista a devolver

    if listaEntrada.count("~") == 0:
        listaSalida = listaEntrada

    else:
        indexNegado = False
        for index in range(len(listaEntrada)):

            if listaEntrada[index] == "~": #Si el elemento es una negación
                listaSalida.append(not listaEntrada[index + 1]) #Niega el siguiente elemento y lo agrega al resultado
                indexNegado = index + 1                         #Guarda el index del valor negado, para no meterlo

            elif index != indexNegado:     #Si no, si el index no es el negado
                listaSalida.append(listaEntrada[index]) #Agregalo


    return listaSalida

def andLogico(listaEntrada):
    listaSalida = [] #Lista a devolver

    if listaEntrada.count("^") == 0:
        listaSalida = listaEntrada

    else:
        for index in range(len(listaEntrada)):
            if (listaEntrada[index] != "^"):
                listaSalida.append(listaEntrada[index])

            elif(listaEntrada[index - 1] == "^"):
                listaSalida.pop()

            else:
                elementoRescatado = listaSalida.pop() #Guardar ultimo elemento de la lista de salida
                listaSalida.append(elementoRescatado and listaEntrada[index + 1])

        if(listaEntrada[len(listaEntrada) - 2] == "^"):
            listaSalida.pop()

    return listaSalida

def orLogico(a,b):
    return a or b

def xorLogico(a,b):
    c = (not a and b) or (a and not b)
    return c

def condicional(a,b):
    return not a or b

def bicondicional(a,b):
    c = condicional(a,b) and condicional(b,a)
    return c

def mapearEcuacion(ecuation, varList, stateList):
    index = 0       #Indice de mapeado
    ecuacionMapeada = []    #Ecuación en lista, para devolver
    for char in ecuation:
        if varList.count(char):     #Si es variable
            index = varList.index(char)     #Encontrar indice
            ecuacionMapeada.append(stateList[index])    #Agregar a la lista a devolver su estado

        else:
            ecuacionMapeada.append(char)    #Devolver operación

    return ecuacionMapeada

def resolverEcuacion(ecuacionEntrada):
    #Función que te deolverá estado lógico
    proceso = [] #Lista que tendrá la ecuación siendo resuelta
    Resultado = [] #Estado Lógico a devolver

    proceso = ecuacionEntrada

    #Resolver parentesis

    #Resolver negaciones
    proceso = negacionLogico(proceso)

    #Resolver and's
    proceso = andLogico(proceso)

    Resultado = proceso
    return Resultado