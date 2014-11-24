#! usr/bin/env python
# -*- coding: latin-1 -*-
numerodepalabras = int(raw_input("Dígame cuántas palabras tiene la primera lista: "))

if numerodepalabras < 1:
    print("¡Imposible!")
else:
    primera = []
    for i in range(numerodepalabras):
        print("Dígame la palabra")
        palabra = raw_input()
        primera += [palabra]
    print("La primera lista es:", primera)

    for i in range(len(primera)-1, -1, -1):
        if primera[i] in primera[:i]:
            del(primera[i])

    numerodepalabras2 = int(raw_input("Dígame cuántas palabras tiene la segunda lista: "))

    if numerodepalabras2 < 1:
        print("¡Imposible!")
    else:
        segunda = []
        for i in range(numerodepalabras2):
            print("Dígame la palabra")
            palabra = raw_input()
            segunda += [palabra]
        print("La segunda lista es:", segunda)

        for i in range(len(segunda)-1, -1, -1):
            if segunda[i] in segunda[:i]:
                del(segunda[i])

        palabrascomunes = []
        for i in primera:
            if i in segunda:
                palabrascomunes += [i]
        print("Palabras que aparecen en las dos listas:", palabrascomunes)

        soloPrimeralista = []
        for i in primera:
            if i not in segunda:
                soloPrimeralista += [i]
        print("Palabras que solo aparecen en la primera lista:", soloPrimeralista)
        
        soloSegundalista = []
        for i in segunda:
            if i not in primera:
                soloSegundalista += [i]
        print("Palabras que solo aparecen en la segunda lista:", soloSegundalista)

        todas = palabrascomunes + soloPrimeralista + soloSegundalista
        print("Todas las palabras:", todas)