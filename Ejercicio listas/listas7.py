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

    for i in range(len(lista)-1, -1, -1):
        if lista[i] in lista[:i]:
            del(lista[i])
    print("La lista sin repeticiones es:", lista)