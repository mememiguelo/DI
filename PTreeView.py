#! /usr/bin/env python
# -*- coding: UTF-8 -*-


# Importamos el módulo pygtk y le indicamos que use la versión 2
import pygtk
pygtk.require("2.0")

# Luego importamos el módulo de gtk y el gtk.glade, este ultimo que nos sirve
# para poder llamar/utilizar al archivo de glade
import gtk
import gtk.glade
import gtk.gdk

class MainWin:

	def __init__(self):
		
		self.widgets  = gtk.glade.XML("Entrega_2.glade")

		window1 = self.widgets.get_widget("dialog1")

		self.vista = self.widgets.get_widget("vista")

		lista=gtk.ListStore(str,int)
		lista.append(["Negro",12])
		lista.append(["Verde",11])
		lista.append(["Blanco",13])

		render=gtk.CellRendererText()
		columna1=gtk.TreeViewColumn("Colores",render,text=0)
		columna2=gtk.TreeViewColumn("Precios",render,text=1)

		self.vista.set_model(lista)
		self.vista.append_column(columna1)
		self.vista.append_column(columna2)
		self.vista.show()


	def on_boton_clicked(self, widget, data=None):
		(model,iter)=self.vista.get_selection().get_selected()
		if iter != None:
			print list(model[iter])

if __name__ == "__main__":
	MainWin()
	gtk.main()