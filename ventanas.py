
import pygtk
#pygtk.require('3.10')
import gtk
from gtk import glade
#glade.XML('Ventana1.glade')
b= gtk.Builder()
b.add_from_file("Ventana1.xml" )
#gtk.main()