#! /usr/bin/env python
# -*- coding: UTF-8 -*-


import pygtk
pygtk.require("2.0")
import gtk
import gtk.glade

# importamos expresiones regulares para validacion
import re

# importamos sqlite
import sqlite3


class Lista:

    def __init__(self):
        self.glade = "Aplicacion_8.glade"
        self.widgets = gtk.Builder()
        self.widgets.add_from_file(self.glade)

        signals = {"on_cdel_activate": self.on_cdel_activate,
                    "on_cEdit_activate": self.on_cEdit_activate,
                    "on_cAdd_activate": self.on_cAdd_activate,
                    "on_cNombrAdd_changed": self.on_cNombrAdd_changed,
                    "on_cApellidoAdd_changed": self.on_cApellidoAdd_changed,
                    "on_cTelefonAdd_changed": self.on_cTelefonAdd_changed,
                    "on_cDioizqAdd_changed": self.on_cDioizqAdd_changed,
                    "on_cDioderAdd_changed": self.on_cDioderAdd_changed,
                    "on_cNombr_changed": self.on_cNombr_changed,
                    "on_cApellido_changed": self.on_cApellido_changed,
                    "on_cTelefon_changed": self.on_cTelefon_changed,
                    "on_cDioizq_changed": self.on_cDioizq_changed,
                    "on_cDioder_changed": self.on_cDioder_changed,
                    "on_about_activate": self.on_about_activate,
                    "gtk_main_quit" : gtk.main_quit }
        
        self.widgets.connect_signals(signals)
        
        # ventana en pantala completa
        self.ventana = self.widgets.get_object('window1')
        self.ventana.maximize()
        
        # Generamos las Lista
        
        # Obtenemos el widget lista
        self.lista = self.widgets.get_object('listaClientes')
        self.model = self.widgets.get_object('modeloClientes')
        
        
        # Indicamos el archivo SQLite
        try:
            self.con = sqlite3.connect('db')
            self.cursor = self.con.cursor()
            
            
        except:
            self.error("La BBDD no esta disponible.\n Confirma que existe el archivo 'db'.")
            
        # Leemos la BBDD nada mas iniciar el programa
        self.leerListaClientes()
        
    def leerListaClientes(self):
        "Leemos la los datos de la BBDD y la insertamos en el arbol"
        # Leemos todos los datos
        self.cursor.execute('SELECT * FROM tClientes')
        
        # Se borra la lista antes por si hay algo
        self.model.clear()
        
        # leemos el sql y rellenamos la lista
        for row in self.cursor:
            self.model.append([row[4], row[5], row[3], row[0], row[1], row[2] ])
        
        # Contamos los clientes y los mostramos
        self.contarClientes()

    def contarClientes(self):
            "Leemos la los datos de la BBDD y la insertamos en el arbol"
            # Leemos todos los datos
            self.cursor.execute('SELECT count(*) FROM tClientes')
            
            self.ctotal = self.widgets.get_object('cTotal')
            
            # leemos el sql y rellenamos la lista
            self.ctotal.set_text(str(self.cursor.fetchone()[0]))

    def on_cdel_activate(self, widget):
        "Evento cuando se pulsa borrar un cliente"
        selection = self.lista.get_selection()
        selection.set_mode(gtk.SELECTION_SINGLE)
        # obtenemos el seleccionado
        self.model, path = selection.get_selected()
        # Si hay seleccionado se muestra el dialogo de confirmacion y se borra
        if(path != None):
            respuesta = self.dialogoBorrar()
            if(respuesta == 1):
                valor = (self.model[path][0],)
                self.cursor.execute('DELETE FROM tClientes WHERE cId=?', valor)
                self.con.commit()
                self.leerListaClientes()
                    
    def on_cEdit_activate(self, widget):
        "Evento cuando se pulsa editar un cliente"
        # obtenemos la lista y el elemento seleccionado
        selection = self.lista.get_selection()
        selection.set_mode(gtk.SELECTION_SINGLE)
        self.model, path = selection.get_selected()
        # si hay algo seleccionado
        if(path != None):
            # Ponemos el nombre actual para saber el cliente editado
            self.clientNombre = self.widgets.get_object("clientNombre")
            self.clientNombre.set_text(self.model[path][1])
            self.clientNombre = self.widgets.get_object("clientApellidos")
            self.clientNombre.set_text(self.model[path][2])
            
            
            
                # Imagenes de validacion
            self.valEdNombre = self.widgets.get_object("valEdNombre")
            self.valEdApellidos = self.widgets.get_object("valEdApellidos")
            self.valEdTelefono = self.widgets.get_object("valEdTelefono")
            self.valEdDioizq = self.widgets.get_object("valEdDioizq")
            self.valEdDioder = self.widgets.get_object("valEdDioder")
            self.imgEdArray = [self.valEdNombre, self.valEdApellidos, self.valEdTelefono, self.valEdDioizq, self.valEdDioder]
            
            # obtenemos los elementos del dialogo y los valores del seleccionado
            self.cNombre = self.widgets.get_object("cNombr")
            self.cNombre.set_text(self.model[path][1])
            self.cApellidos = self.widgets.get_object("cApellido")
            self.cApellidos.set_text(self.model[path][2])
            self.cTelefon = self.widgets.get_object("cTelefon")
            self.cTelefon.set_text(str(self.model[path][3]))
            self.cDioizq = self.widgets.get_object("cDioizq")
            self.cDioizq.set_text(str(self.model[path][4]))
            self.cDioder = self.widgets.get_object("cDioder")
            self.cDioder.set_text(str(self.model[path][5]))
            
            
            # mostramos el dialogo
            respuesta = self.dialogoEditar()
            
            # Ejecuto las verificaciones cada vez que quiero editar
            self.on_cNombr_changed(self)
            self.on_cApellido_changed(self)
            self.on_cTelefon_changed(self)
            self.on_cDioder_changed(self)
            self.on_cDioizq_changed(self)
            
            # leemos el boton pulsado
            if(self.validarDialogo(self.imgEdArray, self.widgets.get_object("aceptar1"))):
                if(respuesta == 1):
                    try:
                        # añadimos los datos del dialog a la BBDD y a la lista 
                        nuevosvalores = (self.cNombre.get_text(), self.cApellidos.get_text(), int(self.cTelefon.get_text()), self.cDioizq.get_text(), self.cDioder.get_text())
                        self.cursor.execute('UPDATE tClientes SET cnombre=?,capellidos=?,ctelefono=?,cdioizquierda=?,cdioderecha=? WHERE cid=' + str(self.model[path][0]), nuevosvalores)
                        self.con.commit()
                        self.leerListaClientes()
                    except:
                        self.error("Por favor introduce valores correctos")
                
    def on_cAdd_activate(self, widget):
        "Evento cuando se pulsa añadir un cliente"
        # obtenemos los elementos del dialogo
        self.cNombreAdd = self.widgets.get_object("cNombrAdd")
        self.cApellidosAdd = self.widgets.get_object("cApellidoAdd")
        self.cTelefonAdd = self.widgets.get_object("cTelefonAdd")
        self.cDioizqAdd = self.widgets.get_object("cDioizqAdd")
        self.cDioderAdd = self.widgets.get_object("cDioderAdd")
            # Imagenes de validacion
        self.valAddNombre = self.widgets.get_object("valAddNombre")
        self.valAddApellidos = self.widgets.get_object("valAddApellidos")
        self.valAddTelefono = self.widgets.get_object("valAddTelefono")
        self.valAddDioizq = self.widgets.get_object("valAddDioizq")
        self.valAddDioder = self.widgets.get_object("valAddDioder")
        self.imgAddArray = [self.valAddNombre, self.valAddApellidos, self.valAddTelefono, self.valAddDioizq, self.valAddDioder]
        
        # Si esta validado leemos el boton pulsado
        respuesta = self.dialogoAdd()
        if(self.validarDialogo(self.imgAddArray, self.widgets.get_object("aceptar2"))):
            if(respuesta == 1):
                try:
                    # añadimos los datos del dialog a la BBDD y a la lista 
                    nuevosvalores = (self.cNombreAdd.get_text(), self.cApellidosAdd.get_text(), int(self.cTelefonAdd.get_text()), self.cDioizqAdd.get_text(), self.cDioderAdd.get_text())
                    self.cursor.execute('INSERT INTO  tClientes(cnombre,capellidos,ctelefono,cdioizquierda,cdioderecha) VALUES (?,?,?,?,?)', nuevosvalores)
                    self.con.commit()
                    self.leerListaClientes()
                except:
                    self.error("Por favor introduce valores correctos")
                    
    def dialogoBorrar(self):
        "Ejecuta el dialogo de confirmacion de borrado de cliente"
        # Obtener el widget del dialogo
        self.dlg = self.widgets.get_object("confirmBorrar")

        # ejecuta el dialogo y espera la respuesta
        self.result = self.dlg.run()
        
        # despues de ejecutado lo esconde
        self.dlg.hide()
        
        # devuelve el boton pulsado
        return self.result
    
    def dialogoEditar(self):
        "Ejecuta el dialogo de editar Cliente"
        # Obtener el widget del dialogo
        self.dlg = self.widgets.get_object("editarDlg")

        # ejecuta el dialogo y espera la respuesta
        self.result = self.dlg.run()
        
        # despues de ejecutado lo esconde
        self.dlg.hide()
        
        # devuelve el boton pulsado
        return self.result
    
    def dialogoAdd(self):
        "Ejecuta el dialogo de Añadir cliente"
        # Obtener el widget del dialogo
        self.dlg = self.widgets.get_object("addDlg")
        
        # Se devuelve todos los valores del dialogo vacio
        self.cNombreAdd = self.widgets.get_object("cNombrAdd")
        self.cNombreAdd.set_text("")
        self.cApellidoAdd = self.widgets.get_object("cApellidoAdd")
        self.cApellidoAdd.set_text("")
        self.cTelefonAdd = self.widgets.get_object("cTelefonAdd")
        self.cTelefonAdd.set_text("")
        self.cDioizqAdd = self.widgets.get_object("cDioizqAdd")
        self.cDioizqAdd.set_text("")
        self.cDioderAdd = self.widgets.get_object("cDioderAdd")
        self.cDioderAdd.set_text("")

        # ejecuta el dialogo y espera la respuesta
        self.result = self.dlg.run()
        
        # despues de ejecutado lo esconde
        self.dlg.hide()
        
        # devuelve el boton pulsado
        return self.result
    
    def error(self, message):
        "Muestra una ventana de error personalizada "
        dialog_error = gtk.MessageDialog(parent=None, flags=0, buttons=gtk.BUTTONS_OK)
        dialog_error.set_title("Error")
        label = gtk.Label(message)
        dialog_error.vbox.pack_start(label, True, True, 0)
        # Con show_all() mostramos el contenido del cuadro de dialogo 
        dialog_error.show_all()
        # El run y destroy hace que la ventana se cierre al apretar el boton
        dialog_error.run()
        dialog_error.destroy()

    def validacion(self, texto, patron, imagenConfirmacion):
        "Valida que un texto coincida con un patron y cambia una imagen a V o X"
        patroncomp = re.compile(patron)
        if(patroncomp.match(texto)):
            imagenConfirmacion.set_from_stock(gtk.STOCK_APPLY, gtk.ICON_SIZE_MENU)
        else:
            imagenConfirmacion.set_from_stock(gtk.STOCK_DIALOG_ERROR, gtk.ICON_SIZE_MENU)
            
    def validarDialogo(self, valores, botonAceptar):
        "Valida si todos los valores de un dialogo son correcto y deja pulsar el boton aceptar"
        for v in valores:
            if(v.get_stock()[0] == None or v.get_stock()[0] == "gtk-dialog-error"):
                botonAceptar.set_sensitive(False)
                return False
        botonAceptar.set_sensitive(True)
        return True

    # Eventos de validacion de los datos introducidos AÑADIR
    def on_cNombrAdd_changed(self, widget):
        self.validacion(self.cNombreAdd.get_text(), r"^[a-zA-Z ]+$", self.valAddNombre)
        self.validarDialogo(self.imgAddArray, self.widgets.get_object("aceptar2"))
    def on_cApellidoAdd_changed(self, widget):
        self.validacion(self.cApellidoAdd.get_text(), r"^[a-zA-Z ]+$", self.valAddApellidos)
        self.validarDialogo(self.imgAddArray, self.widgets.get_object("aceptar2"))
    def on_cTelefonAdd_changed(self, widget):
        self.validacion(self.cTelefonAdd.get_text(), r"^[+\d]+$", self.valAddTelefono)
        self.validarDialogo(self.imgAddArray, self.widgets.get_object("aceptar2"))
    def on_cDioizqAdd_changed(self, widget):
        self.validacion(self.cDioizqAdd.get_text(), r"^-?((2[0-5])|(1[0-9])|\d)(\.\d)?$", self.valAddDioizq)
        self.validarDialogo(self.imgAddArray, self.widgets.get_object("aceptar2"))
    def on_cDioderAdd_changed(self, widget):
        self.validacion(self.cDioderAdd.get_text(), r"^-?((2[0-5])|(1[0-9])|\d)(\.\d)?$", self.valAddDioder)
        self.validarDialogo(self.imgAddArray, self.widgets.get_object("aceptar2"))
        
    # Eventos de validacion de los datos introducidos EDITAR
    def on_cNombr_changed(self, widget):
        self.validacion(self.cNombre.get_text(), r"^[a-zA-Z ]+$", self.valEdNombre)
        self.validarDialogo(self.imgEdArray, self.widgets.get_object("aceptar1"))
    def on_cApellido_changed(self, widget):
        self.validacion(self.cApellidos.get_text(), r"^[a-zA-Z ]+$", self.valEdApellidos)
        self.validarDialogo(self.imgEdArray, self.widgets.get_object("aceptar1"))
    def on_cTelefon_changed(self, widget):
        self.validacion(self.cTelefon.get_text(), r"^[+\d]+$", self.valEdTelefono)
        self.validarDialogo(self.imgEdArray, self.widgets.get_object("aceptar1"))
    def on_cDioizq_changed(self, widget):
        self.validacion(self.cDioizq.get_text(), r"^-?((2[0-5])|(1[0-9])|\d)(\.\d)?$", self.valEdDioizq)
        self.validarDialogo(self.imgEdArray, self.widgets.get_object("aceptar1"))
    def on_cDioder_changed(self, widget):
        self.validacion(self.cDioder.get_text(), r"^-?((2[0-5])|(1[0-9])|\d)(\.\d)?$", self.valEdDioder)
        self.validarDialogo(self.imgEdArray, self.widgets.get_object("aceptar1"))
        
    def on_about_activate(self, widget):
        "Muestra la ventana Acerca de"
        about = gtk.AboutDialog()
        about.set_name("Gestor de Optica")
        about.set_version("1.0")
        about.set_comments("Gestiona los clientes y productos de tu optica.")
        about.set_copyright("IES Chan Do Monte")
        
        def openHomePage(widget, url, url2):  # Para abrir el sitio
            import webbrowser
            webbrowser.open_new(url)
        
        gtk.about_dialog_set_url_hook(openHomePage, "http://dawdamasir.com/")
        about.set_website("http://dawdamasir.com/")
        about.set_authors(["Joaquin Casas Marino (jcasamari)"])
        about.run()
        about.destroy()
        
            
if __name__ == "__main__":
    Lista()
    gtk.main()
