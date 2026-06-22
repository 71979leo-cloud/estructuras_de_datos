import sys
from PyQt5 import QtWidgets, uic

# Importación directa y limpia como te la enseñaron
from estructuras.lineales.lista_enlazada_simple import LinkedList

class VentanaLista(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        
        # Cargamos la interfaz gráfica usando la ruta directa desde la raíz
        uic.loadUi("ui/funciones_lista.ui", self)
        
        # Instanciamos el motor de la lista enlazada
        self.lista = LinkedList()
        
        # ========================================================
        # CONEXIÓN DE LOS BOTONES
        # ========================================================
        self.btn_agregar_inicio.clicked.connect(self.metodo_agregar_inicio)
        self.btn_agregar_final.clicked.connect(self.metodo_agregar_final)
        self.btn_imprimir.clicked.connect(self.metodo_imprimir)
        self.btn_eliminar_inicio.clicked.connect(self.metodo_eliminar_inicio)
        self.btn_eliminar_final.clicked.connect(self.metodo_eliminar_final)
        self.btn_buscar.clicked.connect(self.metodo_buscar)

    # ========================================================
    # FUNCIONES QUE SE ENLAZAN A TU LÓGICA
    # ========================================================
    
    def metodo_agregar_inicio(self):
        dato = self.txt_dato.text()
        if dato:
            self.lista.insert_at_beginning(dato)
            self.lbl_resultado.setText(f"Agregado al inicio: {dato}")
            self.txt_dato.clear()
        else:
            self.lbl_resultado.setText("Escribe un dato primero")

    def metodo_agregar_final(self):
        dato = self.txt_dato.text()
        if dato:
            self.lista.insert_at_end(dato)
            self.lbl_resultado.setText(f"Agregado al final: {dato}")
            self.txt_dato.clear()
        else:
            self.lbl_resultado.setText("Escribe un dato primero")

    def metodo_imprimir(self):
        self.lista.print_linked_list()
        self.lbl_resultado.setText("Lista impresa en consola")

    def metodo_eliminar_inicio(self):
        self.lista.delete_at_beginning()
        self.lbl_resultado.setText("Se eliminó el primer elemento")

    def metodo_eliminar_final(self):
        self.lista.delete_at_end()
        self.lbl_resultado.setText("Se eliminó el último elemento")

    def metodo_buscar(self):
        dato = self.txt_dato.text()
        if dato:
            encontrado = self.lista.search(dato)
            if encontrado:
                self.lbl_resultado.setText(f"El elemento {dato} SÍ existe")
            else:
                self.lbl_resultado.setText(f"El elemento {dato} NO existe")
        else:
            self.lbl_resultado.setText("Escribe el dato a buscar")