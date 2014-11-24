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
	for i in range(0,maximotablero):
		for x in range(0,maximofila):
			sys.stdout.write(tablero[i][x])
		print (i+1)
	print(" 1  2  3  4  5  6  7  8  9 ")

def seleccionarJugador():
	correcto=0
	global jugador
	global maquina
	while correcto<1:
		valor=raw_input('Selecciona el jugador X o O') #en version de python 3.+ utilizar "input" en lugar de "raw_input"
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
				print ("El caracter seleccionado no es correcto")

def hacerTiradaMaquina():
	print ("")
	tiradax =  random.randrange(9)
	#tiradax=int(raw_input('Columna por la que quieres tirar || 0 para salir '))
	contador2=0
	tiradax = tiradax -1
	for z in range(0,maximotablero):
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
		tiradax=int(input('Columna por la que quieres tirar || 0 para salir '))
		if tiradax!=0:
			contador=0
			tiradax = tiradax -1
			for z in range(0,maximotablero):
				if(tablero[z][tiradax] == '|_|' ):
					#print 'Esta libre'
					contador += 1
			contador = contador - 1
			#print contador
			tablero[contador][tiradax] = '|'+jugador+'|'
			tiradax = tiradax +1
			imprimirTablero()
			resultado = comprobartablero(jugador)
			if (resultado == True):
				tiradax=0
				print("GANA EL JUGADOR")
			else:
				hacerTiradaMaquina()
			resultado2 = comprobartablero(maquina)
			if (resultado2 == True):
				tiradax=0
				print("GANA LA MAQUINA")

def comprobartablero(elemento):
	comprobar = "|"+elemento+"|"
	resultado = False
	contador=1
	for y in range(0,maximotablero):
		for x in range(0,maximofila):
			if(tablero[y][x] == comprobar): #Encuentro la posicion donde hay una ficha , tengo que mirar en todas las direcciones
				
				z=0
				for z in range(0,3): #compruebo si hay tres fichas iguales por su derecha en horizontal
					z=z+1
					if(x+z<9):
						if(tablero[y][x+z]==comprobar):
							contador+=1
				if (contador==4):
					print ('Hay cuatro en raya hacia la derecha que empieza en %s y %s' %(10-y,10-x))
					resultado = True
				contador=1
				z=0
				for z in range(0,3): #compruebo si hay tres fichas iguales por su derecha en diagonal hacia abajo
					z=z+1
					if(x+z<9 and y+z<9):
						if(tablero[y+z][x+z]==comprobar):
							contador+=1
				if (contador==4):
					print ('Hay cuatro en raya hacia la derecha diagonal descendente que empieza en %s y %s' %(10-y,10-x))
					resultado = True
				contador=1
				z=0
				for z in range(0,3):
					z=z+1
					if(y+z<9):
						if (tablero[y+z][x]==comprobar):
							contador+=1
				if (contador==4):
					print ('Hay cuatro en raya hacia abajo que empieza en %s y %s' %(10-y,10-x))
					resultado = True
				contador=1
				z=0
				for z in range(0,3):
					z=z+1
					if(x-z>0 and y+z<9):
						if(tablero[y+z][x-z]==comprobar):
							contador+=1
				if (contador==4):
					print ('Hay cuatro en raya hacia la izquierda diagonal descendente que empieza en %s y %s' %(10-y,10-x))
					resultado = True
				contador=1
	return resultado


def main():
	seleccionarJugador()
	print ("Eres el jugador "+ jugador)
	imprimirTablero()
	hacerTiradaJugador()

main()