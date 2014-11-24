#! /usr/bin/env python
# -*- coding: UTF-8 -*-


# Importamos el módulo pygtk y le indicamos que use la versión 2
import pygtk
import gtk
import math
pygtk.require("2.0")

# Luego importamos el módulo de gtk y el gtk.glade, este ultimo que nos sirve
# para poder llamar/utilizar al archivo de glade
import gtk
import gtk.glade
import gtk.gdk

class MainWin:

	def __init__(self):
		# Le decimos a nuestro programa que archivo de glade usar (puede tener
		# un nombre distinto del script). Si no esta en el mismo directorio del
		# script habría que indicarle la ruta completa en donde se encuentra
		self.widgets  = gtk.glade.XML("EjercicioPorcentajes.glade")
		self.widgetss = gtk.glade.XML("about.glade")
		self.widgetsss = gtk.glade.XML("error.glade")

		window1 = self.widgets.get_widget("window1")
		window2 = self.widgetss.get_widget("aboutdialog1")
		window3 = self.widgetsss.get_widget("window1")

		#Color de fondo
		window1.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color('#A3FF9C'))

		# Creamos un pequeño diccionario que contiene las señales definidas en
		# glade y su respectivo método (o llamada)
		signals = {"on_entry2_changed" : self.calcular,
			"on_combobox1_changed": self.calcular,
			"on_closeitem_activate": self.closeWindow,
			"on_acercadeitem_activate": self.aboutWindow,
			"gtk_main_quit" : gtk.main_quit }
		signals2 = {"on_button1_activate": self.cerrarWindowError,
			"gtk_main_quit" : self.cerrarWindowError }

		# Luego se auto-conectan las señales.
		self.labelPrecio = self.widgets.get_widget("labelPrecio")
		self.labelDescontado = self.widgets.get_widget("labelDescontado")
		self.combobox1 = self.widgets.get_widget("combobox1")
		self.combobox1.set_active(1)
		
		
		self.widgets.signal_autoconnect(signals)
		self.widgetsss.signal_autoconnect(signals2)

	def calcular(self,widgets):
		numero = self.widgets.get_widget("entry2").get_text()
		descuento = self.widgets.get_widget("combobox1")

		if(self.isNaN(numero) and numero):
			ventana = self.widgetsss.get_widget("window1")
			ventana.show()
			#ventana.hide()
		else:
			#print(int(numero)+int(numero))
			if(len(numero)==0):
				numero = 0;
			descuento = descuento.get_model()[descuento.get_active()][0]
			totalDescontado = float(numero)*float(descuento)/100
			#print(total)
			total = float(numero)-float(totalDescontado)
			self.labelPrecio.set_text(str(total))
			self.labelDescontado.set_text(str(totalDescontado))

	def closeWindow(self,widgets):
		#print("Cerrar ventana")
		#window1.destroy()
		self.widgets.get_widget("window1").destroy()

	def aboutWindow(self,widgets):
		#print("Acerca de  Ventana")
		self.widgetss.get_widget("aboutdialog1").show_all()


	def cerrarWindowError(self,widgets):
		#print("cerrar")
		self.widgetsss.get_widget("window1").hide()


	def isNaN(self,value):
		try:
			float(value)
			return False
		except ValueError:
			return True

if __name__ == "__main__":
	MainWin()
	gtk.main()
