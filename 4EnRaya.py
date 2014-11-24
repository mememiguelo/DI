#! usr/bin/env python

import sys
import random

#print "|_||_||_||_||_||_||_||_|";
#print "|_||_||_||_||_||_||_||_|";
#print "|_||_||_||_||_||o||_||_|";
#print "|_||_||_||o||o||x||_||_|";
#print "|_||_||_||o||x||x||o||_|";
#print "|_||_||o||x||x||x||o||_|";
jugador=""
maquina=""
fila1=['|_|','|_|','|_|','|_|','|_|','|_|','|_|','|_|','|_|']
fila2=['|_|','|_|','|_|','|_|','|_|','|_|','|_|','|_|','|_|']
fila3=['|_|','|_|','|_|','|_|','|_|','|_|','|_|','|_|','|_|']
fila4=['|_|','|_|','|_|','|_|','|_|','|_|','|_|','|_|','|_|']
fila5=['|_|','|_|','|_|','|_|','|_|','|_|','|_|','|_|','|_|']
fila6=['|_|','|_|','|_|','|_|','|_|','|_|','|_|','|_|','|_|']
fila7=['|_|','|_|','|_|','|_|','|_|','|_|','|_|','|_|','|_|']
fila8=['|_|','|_|','|_|','|_|','|_|','|_|','|_|','|_|','|_|']
fila9=['|_|','|_|','|_|','|_|','|_|','|_|','|_|','|_|','|_|']
maximofila = len(fila1)

tablero = [fila1,fila2,fila3,fila4,fila5,fila6,fila7,fila8,fila9]
maximotablero = len(tablero)

def imprimirTablero():	
	for i in xrange(0,maximotablero):
		for x in xrange(0,maximofila):
			sys.stdout.write(tablero[i][x])
		print ''

def seleccionarJugador():
	correcto=0
	global jugador
	global maquina
	while correcto<1:
		valor=raw_input('Selecciona el jugador X o O')
		if(valor == 'X'):
			jugador = 'X'
			maquina = 'O'
			correcto=1
		else:
			if(valor == 'O'):
				jugador = 'O'
				maquina = 'X'
				correcto=1
			else:
				print "El caracter seleccionado no es correcto"

def hacerTiradaMaquina():
	print ""
	tiradax =  random.randrange(9)
	#tiradax=int(raw_input('Columna por la que quieres tirar || 0 para salir '))
	contador2=0
	tiradax = tiradax -1
	for z in xrange(0,maximotablero):
		if(tablero[z][tiradax] == '|_|' ):
			#print 'Esta libre'
			contador2 += 1
			#print contador2
	contador2 = contador2 - 1
	#print contador2
	#print tiradax
	tablero[contador2][tiradax] = '|'+maquina+'|'
	imprimirTablero()

def hacerTiradaJugador():
	tiradax=1
	while tiradax!=0:
		tiradax=int(raw_input('Columna por la que quieres tirar || 0 para salir '))
		if tiradax!=0:
			contador=0
			tiradax = tiradax -1
			for z in xrange(0,maximotablero):
				if(tablero[z][tiradax] == '|_|' ):
					#print 'Esta libre'
					contador += 1
			contador = contador - 1
			#print contador
			tablero[contador][tiradax] = '|'+jugador+'|'
			tiradax = tiradax +1
			imprimirTablero()
			comprobartablero()
			#hacerTiradaMaquina()

def comprobartablero():
	contador=1
	for y in xrange(0,maximotablero):
		for x in xrange(0,maximofila):
			if(tablero[y][x] == "|X|"):
				z=0
				total = 0
				global total
				for z in xrange(0,3):
					z=z+1
					if(x+z>9):
						total = (z+1)-x
					else:
						total=x+z
					if(tablero[y][x-z]=="|X|"):
						contador+=1
				print contador
				if (contador==4):
					print 'Hay cuatro en raya hacia la izquierda que empieza en %s y %s' %(y,x)
				contador=1


def main():
	seleccionarJugador()
	print "Eres el jugador "+ jugador
	#hacerTiradaMaquina()
	imprimirTablero()
	hacerTiradaJugador()

main()