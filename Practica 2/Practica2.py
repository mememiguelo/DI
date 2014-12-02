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
import sqlite3

conn = sqlite3.connect('tEjercicio')
c = conn.cursor()


# Creamos la clase de la ventana principal del programa
class MainWin:

	def __init__(self):
		# Le decimos a nuestro programa que archivo de glade usar (puede tener
		# un nombre distinto del script). Si no esta en el mismo directorio del
		# script habría que indicarle la ruta completa en donde se encuentra
		self.widgets  = gtk.glade.XML("Entrega_2.glade")

		window1 = self.widgets.get_widget("window1")
		self.window2 = self.widgets.get_widget("dialog1")

		self.vista = self.widgets.get_widget("vista")

		#Color de fondo
		window1.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color('#F8E0F7'))

		# Creamos un pequeño diccionario que contiene las señales definidas en
		# glade y su respectivo método (o llamada)
		signals = {"on_button1_clicked" : self.on_button1_clicked,
			"onClickGrabar" : self.onClickGrabar,
			"onClickListar" : self.onClickListar,
			"gtk_main_quit" : gtk.main_quit }

		# Luego se auto-conectan las señales.
		self.widgets.signal_autoconnect(signals)

	# Se definen los métodos, en este caso señales como "destroy" ya fueron
	# definidas en el .glade, así solo se necesita definir "on_button1_clicked"
	def on_button1_clicked(self, widget):
		"Muestra la ventana con los datos"

		

		ventana = gtk.Dialog()
		ok_button = ventana.add_button(gtk.STOCK_OK, gtk.RESPONSE_OK)
		cancelar_button = ventana.add_button(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL)
		ok_button.grab_default()
		ventana.set_title("Confirma")
		label = gtk.Label("<b>¿Guardar Datos?</b>\n")
		label.set_property("use-markup", True)
		entry1 = gtk.Label("Usuario: "+self.widgets.get_widget("entry1").get_text())
		entry2 = gtk.Label("Contraseña: "+self.widgets.get_widget("entry2").get_text())
		entry3 = gtk.Label("E-mail: "+self.widgets.get_widget("entry3").get_text())
		entry4 = gtk.Label("Nombres: "+self.widgets.get_widget("entry4").get_text())
		entry5 = gtk.Label("Apellidos: "+self.widgets.get_widget("entry5").get_text())

		#Obtenemos datos del textview
		textview1 = self.widgets.get_widget("textview1")
		buffer = textview1.get_buffer()
		textview = gtk.Label("Direccion: "+buffer.get_text(buffer.get_start_iter(),buffer.get_end_iter())+"\n\n")

		ventana.vbox.pack_start(label, True, True, 0)
		ventana.vbox.pack_start(entry1, True, True, 0)
		ventana.vbox.pack_start(entry2, True, True, 0)
		ventana.vbox.pack_start(entry3, True, True, 0)
		ventana.vbox.pack_start(entry4, True, True, 0)
		ventana.vbox.pack_start(entry5, True, True, 0)
		ventana.vbox.pack_start(textview, True, True, 0)


		# Con show_all() mostramos el contenido del cuadro de dialogo (en este
		# caso solo tiene la etiqueta) si no se hace el dialogo aparece vacio
		ventana.show_all()
		# El run y destroy hace que la ventana se cierre al apretar el boton
		ventana.run()
		ventana.destroy()

	def onClickGrabar(self,widget):
		#print("guarda los datos")
		usuario = self.widgets.get_widget("entry1").get_text()
		contrasena = self.widgets.get_widget("entry2").get_text()
		email = self.widgets.get_widget("entry3").get_text()
		nombre = self.widgets.get_widget("entry4").get_text()
		apellidos = self.widgets.get_widget("entry5").get_text()

		textview1 = self.widgets.get_widget("textview1")
		buffer = textview1.get_buffer()
		direccion = buffer.get_text(buffer.get_start_iter(),buffer.get_end_iter())

		c.execute('insert into tusuario(usuario,contraseña,email,nombre,apellidos,direccion) values ("'+str(usuario)+'","'+str(contrasena)+'","'+str(email)+'","'+str(nombre)+'","'+str(apellidos)+'","'+str(direccion)+'")')
		conn.commit()

	def onClickListar(self,widget):
		#print("Listar datos")

		#self.widgets  = gtk.glade.XML("Entrega_2.glade")

		#self.window2.clear()

		self.lista=gtk.ListStore(str,str,str,str,str,str,)

		self.lista.clear()
		c.execute('SELECT * FROM tusuario;')

		for x in c.fetchall():
			self.lista.append([x[0],x[1],x[2],x[3],x[4],x[5]])
		
		
		render=gtk.CellRendererText()
		columna1=gtk.TreeViewColumn("Usuario",render,text=0)
		columna2=gtk.TreeViewColumn("Contraseña",render,text=1)
		columna3=gtk.TreeViewColumn("Email",render,text=2)
		columna4=gtk.TreeViewColumn("Nombre",render,text=3)
		columna5=gtk.TreeViewColumn("Apellidos",render,text=4)
		columna6=gtk.TreeViewColumn("Direccion",render,text=5)



		self.vista.set_model(self.lista)
		self.vista.append_column(columna1)
		self.vista.append_column(columna2)
		self.vista.append_column(columna3)
		self.vista.append_column(columna4)
		self.vista.append_column(columna5)
		self.vista.append_column(columna6)
		self.vista.show()

		self.window2.show_all()
		self.window2.run()
		self.window2.hide();

		

# Para terminar iniciamos el programa
if __name__ == "__main__":
	MainWin()
	gtk.main()
