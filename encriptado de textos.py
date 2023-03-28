"""
Ejercicios finales
Eduardo Garcia Castrejón
Fisica 1A
Programa 2
CRIPTOGRAFIA
"""
import string
# -*- coding: utf-8 -*-
def variable(opz):
    while True:
        opz = input()
        if len(opz) != 1 or opz not in '123':
            print("Favor de introducir solo un numero: ")
        else:
            return int(opz)
            
opz = 1
opc = 1
while opc != 3:
#Menu
    print("Menu")
    print("1. Codificar texto")
    print("2. Decodificar texto")
    print("3. Salir")
    print("Introduce una opción: ")
    opc = variable(opz)

#codificar
    if opc == 1:
        print("1. Leer archivo .txt")
        print("2. Escribir texto")
        print("3. Salir")
        print("Introduce una opción: ")
        q = []
        opc1 = int(input())
        if opc1 == 3:
            break
        n = int(input("Código de encriptación (número): "))
        tildes = "áéíóúñ"
        tildesMa = "ÁÉÍÓÚÑ"

    #leer archivo1


        if opc1 == 1:
            v = input("¿Nombre del archivo txt? ")
            f = open('{0}.txt'.format(v),'r')
        #filenotfound?
            p = f.read()
            f.close()
            print(p)
    
    #Escribir texto
        elif opc1 == 2:
            p = input("Introduzca el texto: ")
        else:
            opc = 3
        for x in range(0,len(p)):
    
    #espacios
            if p[x] in string.punctuation or p[x] in string.whitespace:
                q.append(p[x])

    #minusculas
            if p[x] in string.ascii_lowercase:
                minus = ord(p[x]) + n
                a = 122 - ord(p[x])
                b = n - a                
                while minus > 122:
                    minus = 96 + b
                    b -= 26
                minus_cod = chr(minus)
                q.append(minus_cod)

    #mayus
            if p[x] in string.ascii_uppercase:
                max = ord(p[x]) + n
                a = 90 - ord(p[x])
                b = n - a
                while max > 90:
                    max = 64 + b
                    b -= 26
                max_cod = chr(max)
                q.append(max_cod)

    #numeros
            if p[x] in string.digits:
                num = ord(p[x]) + n
                a = 57 - ord(p[x])
                b = n - a    
                while num > 57:
                    num = 47 + b
                    b -= 10
                num_cod = chr(num)
                q.append(num_cod)

    #tildes
            if p[x] in tildes:
                tild = tildes.find(p[x]) 
                if tild >= 0:
                    tild_cod = tild + n
                    a = 6 - tild 
                    b = n - a
                    while tild_cod >= 6:
                        tild_cod = b
                        b -= 6
                    q.append(tildes[tild_cod])
            if p[x] in tildesMa:
                TILD = tildesMa.find(p[x])
                if TILD >= 0:
                    TILD_cod = TILD + n
                    a = 6 - TILD 
                    b = n - a
                    while TILD_cod >= 6:
                        TILD_cod = b
                        b -= 6
                    q.append(tildesMa[TILD_cod]) 

        p = "".join(q)
        print("Su texto codificado está listo, ¿Desea guardarlo en un .txt?")
        print("1. Sí\n2. No")
        opc2 = int(input())
        if opc2 == 1:
            d = input("¿Cómo deseas guardar el archivo .txt? ")
            g = open('{0}.txt'.format(d),'w')
            g.write(p)
            g.close()
        else:
            print("Texto codificado: ",p,)
    

#Decodificar
    if opc == 2:
        print("1. Leer archivo encriptado .txt")
        print("2. Escribir texto encriptado")
        print("3. Salir")
        print("Introduce una opción: ")
        q = []
        opc1 = int(input())
        if opc1 == 3:
            break
        n = int(input("Código de encriptación(número): "))
        tildes = "áéíóúñ"
        tildesMa = "ÁÉÍÓÚÑ"

    #Leer archivo
        if opc1 == 1:
            v = input("¿Nombre del archivo txt? ")
            f = open('{0}.txt'.format(v),'r')
        #filenotfound?
            p = f.read()
            f.close()
            print(p)

    #Escribir texto
        elif opc1 == 2:
            p = input("Introduzca el texto: ")
        else:
            opc = 3
        for x in range(0,len(p)):

    #espacios
            if p[x] in string.punctuation or p[x] in string.whitespace:
                q.append(p[x])

    #minusculas
            if p[x] in string.ascii_lowercase:
                minus = ord(p[x]) - n
                a = ord(p[x]) - 97
                b = n - a
                while minus < 97:
                    minus = 123 - b
                    b -= 26
                minus_cod = chr(minus)
                q.append(minus_cod)

    #mayus
            if p[x] in string.ascii_uppercase:
                max = ord(p[x]) - n
                a = ord(p[x]) - 65
                b = n - a
                while max < 65:
                    max = 91 - b
                    b -= 26
                max_cod = chr(max)
                q.append(max_cod)

    #numeros
            if p[x] in string.digits:
                num = ord(p[x]) - n
                a = ord(p[x]) - 48
                b = n - a    
                while num < 48:
                    num = 58 - b
                    b -= 10
                num_cod = chr(num)
                q.append(num_cod)

    #tildes
            if p[x] in tildes:
                tild = tildes.find(p[x])
                if tild >= 0:
                    tild_cod = tild - n 
                    b = n - tild
                    while tild_cod < 0:
                        tild_cod = 6 - b
                        b -= 61
                    q.append(tildes[tild_cod])

            if p[x] in tildesMa:          
                TILD = tildesMa.find(p[x]) 
                if TILD >= 0:
                    TILD_cod = TILD - n 
                    b = n - TILD
                    while TILD_cod < 0:
                        TILD_cod = 6 - b
                        b -= 6
                    q.append(tildesMa[TILD_cod])

        p = "".join(q)
        print("Su texto descodificado está listo, ¿Desea guardarlo en un .txt?")
        print("1. Sí\n2. No")
        opc2 = int(input())
        if opc2 == 1:
            d = input("¿Cómo deseas guardar el archivo .txt? ")
            g = open('{0}.txt'.format(d),'w')
            g.write(p)
            g.close()
        else:
            print("Texto descodificado: ",p,)