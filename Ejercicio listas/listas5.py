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

    numerodepalabras2 = int(raw_input("Dígame cuántas palabras tiene la lista de palabras a eliminar: "))

    if numerodepalabras2 < 1:
        print("¡Imposible!")
    else:
        palabraeliminar = []
        for i in range(numerodepalabras2):
            print("Dígame la palabra")
            palabra = raw_input()
            palabraeliminar += [palabra]
        print("La lista de palabras a eliminar es:", palabraeliminar)

        for i in palabraeliminar:
            for j in range(len(lista)-1, -1, -1):
                if lista[j] == i:
                    del(lista[j])
        print("La lista es ahora:", lista)