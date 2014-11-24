#! usr/bin/env python
# -*- coding: latin-1 -*-
numerodepalabras = int(raw_input("Dígame cuántas palabras tiene la lista: "))

if numerodepalabras < 1:
    print("¡Imposible!")
else:
    lista = []
    for i in range(numerodepalabras):
        print("Dígame la palabra")
        palabra = raw_input()
        lista += [palabra]
    print("La lista creada es:", lista)

    palabraparabuscar = raw_input("Sustituir la palabra: ")
    palabraparasustituir = raw_input("por la palabra: ")
    for i in range(len(lista)):
        if lista[i] == palabraparabuscar:
            lista[i] = palabraparasustituir
    print("La lista es ahora:", lista)