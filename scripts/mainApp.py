# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 14:09:22 2023

@author: User
"""

#Import PyQT5 elements
from PyQt5 import uic #Importas el modulo para la carga de las interfaces
from PyQt5.QtWidgets import QMainWindow, QApplication, QTabWidget, QTreeWidget 
from PyQt5.QtCore import QCoreApplication

#Import functions and other imports
import listaDeTemas as LDT
import sys
import easygui as eg


class MyGUI(QMainWindow):
    ''' Defino una clase para importar la GUI creada con QtDesigner'''
    # def __init__(self):
    #     super(MyGUI, self).__init__()
    #     uic.loadUi("interfaz_grafica_listaDeTemas.ui", self) # Carga la interfaz que debe estar en el mismo directorio que este archivo que la corre.
    
    def __init__(self):
        super().__init__()
        uic.loadUi("interfaz_grafica_listaDeTemas.ui", self) # Carga la interfaz

        #-***-***-***-***-***-***  
        # --- BOTONES ---
        #-***-***-***-***-***-***
        
        #Tecla cerrar GUI
        self.btn_cerrarGUI.clicked.connect(QCoreApplication.instance().quit) #Kills the program
        self.btn_cerrarGUI.clicked.connect(self.cerrarWindow) #Closes the window

        #Boton dir entrada y salida
        self.btn_dirs.clicked.connect(self.setearDirectorios)
        
        #Check box para sortear el texto, devuelve True si esta clickeado
        if self.chbox_sorted.isChecked():
            self.sort_por_genero = True
        else:
            self.sort_por_genero = False
   
        #Boton que ejecuta las fc que generan la lista en txt. 
        self.btn_getTheList.clicked.connect(self.getMyList)
        
        #Boton about me
        self.btn_aboutMe.clicked.connect(self.showAboutMe)
    
    #Boton que abre ventanas p setear directorios.
    #Ademas, solo desp de ejecutar esta fc, ie,  existen DIR_IN y DIR_OUT, 
    #se habilita a clickear el boton 'get list'.
    def setearDirectorios(self):
        #Seteo directorios.
        self.DIR_IN =  eg.diropenbox(msg="Choose directory with folders with music files", title="Select in directory")
        self.DIR_OUT =  eg.diropenbox(msg="Select directory to store txt list", title="Select out directory")
        
        #Una vez que estan establecidos DIR_IN y DIR_OUT, imprimo en los labels correspondientes
        #los paths para que los vea el usuario. Muestro los ultimos caracteres del path por las dudas.
        self.txt_inDir.setText(self.DIR_IN)
        self.txt_outDir.setText(self.DIR_OUT)
        
        #Por ultimo habilito el boton 'get list'
        self.btn_getTheList.setEnabled(True)
    
    #-***-***-***-***-***-***  
    # --- FUNCIONES ---
    #-***-***-***-***-***-***
    def getMyList(self):
        self.listaDeTemas = LDT.generarLista(self.DIR_IN, self.sort_por_genero, LDT.tab_cancion, LDT.tab_entre_bandas, LDT.indice_de_generos)
        LDT.guardarTXT(self.DIR_OUT, self.listaDeTemas)
        self.label_todoOK.setText('List has been\ncreated successfully!')


    def cerrarWindow(self):
        self.close()

    def showAboutMe(self):
        '''Levanta un cartel con about me.'''
        mensaje = '''
            _________    
            About me
            _________
        
            
            App created by Yair Barnatan
            Visit: 
                *  https://www.linkedin.com/in/yair-barnatan-b66985a6/
                *  https://ybarnatan.github.io/
        '''
        eg.msgbox(msg=mensaje,
                  title='ABOUT ME', 
                  ok_button='Close this message.')

#%% Correr el programa entero: GUI + back end.

def main():
    app = QApplication(sys.argv) #Crear la aplicación
    GUI = MyGUI()  #Crear el objeto que carga la interfaz
    GUI.show() #Mostrar la interfaz
    sys.exit(app.exec_()) #función exit del módulo sys para que al presionar la "x" roja de la ventana se cierre correctamente    
    

if __name__ == '__main__':
    main()
