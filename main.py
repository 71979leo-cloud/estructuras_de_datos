import sys
from PyQt5 import QtWidgets, uic

# Importamos tu archivo de lógica dentro de la carpeta load
import load.load_lista_enlazada as interfaz_lista

class MainWindowPrincipal(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Cargamos tu interfaz de la ventana principal (el menú superior)
        uic.loadUi("ui/lista_enlazada.ui", self)
        
        # Conexión para la opción de menú "Lista Enlazada"
        self.actionLista_Enlazada.triggered.connect(self.abrir_dialogo_funciones)

    def abrir_dialogo_funciones(self):
        # Llamamos exactamente a tu clase real: VentanaLista
        dialogo = interfaz_lista.VentanaLista()
        dialogo.exec_() 

def main():
    app = QtWidgets.QApplication(sys.argv)
    ventana_principal = MainWindowPrincipal()
    ventana_principal.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()