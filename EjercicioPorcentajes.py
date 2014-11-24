#! /usr/bin/env python
# -*- coding: UTF-8 -*-


# Importamos el módulo pygtk y le indicamos que use la versión 2
import pygtk
import gtk
pygtk.require("2.0")

# Luego importamos el módulo de gtk y el gtk.glade, este ultimo que nos sirve
# para poder llamar/utilizar al archivo de glade
import gtk
import gtk.glade
import gtk.gdk




def porcentaje5(valor):
	
   	resultado=valor/100
	resultado2=resultado*5
	resultado3 = valor-resultado2
	return resultado3


def porcentaje10(valor):

   	resultado=valor/100
	resultado2=resultado*10
	resultado3 = valor-resultado2
	return resultado3



def porcentaje20(valor):

   	resultado=valor/100
	resultado2=resultado*20
	resultado3 = valor-resultado2
	return resultado3

# Función que obtiene el texto de la opción seleccionada en un ComboBox
def valor_combobox(combobox):
	model = combobox.get_model()
	activo = combobox.get_active()
	if activo <0:
		return None
	return model[activo][0]


def error(message):
        "Display the error dialog "
        dialog_error = gtk.MessageDialog(parent=None, flags=0, buttons=gtk.BUTTONS_OK)
        dialog_error.set_title("Error")
        label = gtk.Label(message)
        dialog_error.vbox.pack_start(label, True, True, 0)
        # Con show_all() mostramos el contenido del cuadro de dialogo (en este
        # caso solo tiene la etiqueta) si no se hace el dialogo aparece vacío
        dialog_error.show_all()
        # El run y destroy hace que la ventana se cierre al apretar el botón
        dialog_error.run()
        dialog_error.destroy()

# Creamos la clase de la ventana principal del programa
class MainWin:
	
	def __init__(self):
		
		self.widgets  = gtk.glade.XML("EjercicioPorcentajes.glade")

		window1 = self.widgets.get_widget("window1")
		self.entry2 = self.widgets.get_widget("entry2")
		self.labelPrecio = self.widgets.get_widget("labelPrecio")

		#Color de fondo
		window1.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color('#F5BCA9'))

		# Creamos un pequeño diccionario que contiene las señales definidas en
		# glade y su respectivo método (o llamada)
		signals = {"on_entry2_changed" : self.calcular,
			"gtk_main_quit" : gtk.main_quit
			 }


		self.combobox1 = self.widgets.get_widget("combobox1")
		self.combobox1.set_active(1)


		# Luego se auto-conectan las señales.
		self.widgets.signal_autoconnect(signals)




	def calcular(self, widget):
		 # Se crea un buffer en donde se guardaran los resultados
		text_buffer = gtk.TextBuffer()
		# Se obtiene el valor para convertir desde la entrada
		valor = self.entry2.get_text()		

		# Obtiene la opción escogida en el ComboBoxs
		seleccion = valor_combobox(self.combobox1)

		precio_ini = float(valor)
		    

		if seleccion == "5":
			precio=(str(porcentaje5(precio_ini)))
		elif seleccion == "10":
		        precio=(str(porcentaje10(precio_ini)))
		elif seleccion == "20":
		        precio=(str(porcentaje20(precio_ini)))
		    
		else:
		        # Se produce cuando las dos selecciones son iguales
		        error("The initial and target units are the same")
		    

		self.set.labelPrecio(precio)
        
		
# Para terminar iniciamos el programa
if __name__ == "__main__":
	MainWin()
	gtk.main()
