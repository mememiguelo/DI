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

    palabraparabuscar = raw_input("Dígame la palabra a buscar: ")
    contador = 0
    for i in lista:
        if i == palabraparabuscar:
            contador += 1;
    if contador == 0:
        print("La palabra '" + palabraparabuscar + "' no aparece en la lista.")
    elif contador == 1:
        print("La palabra '" + palabraparabuscar + "' aparece una vez en la lista.")
    else:    
        print("La palabra '" + palabraparabuscar + "' aparece", contador, "veces en la lista.")