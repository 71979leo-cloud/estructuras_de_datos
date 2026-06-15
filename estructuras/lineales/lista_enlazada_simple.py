from estructuras.lineales.nodo import Node

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_at_beginning(self, data):
        #Paso 1: Crear un nuevo nodo con el dato proporcionado
        new_node = Node(data)

        #Paso 2: Verificar si la lista está vacía
        if self.head is None and self.tail is None:
            #Si la lista está vacía, el nuevo nodo se convierte en la cabeza y la cola
            self.head = new_node
            self.tail = new_node
        else:
            #Si la lista no está vacía, el nuevo nodo apunta a la cabeza actual
            new_node.next = self.head
            #Luego, la cabeza se actualiza para ser el nuevo nodo
            self.head = new_node
    
    def print_linked_list(self):
        temp = self.head
        print("Head ->", end="")
        while temp is not None:
            print(temp.data,"->", end="")
            temp = temp.next
        print("<- Tail")

    def insert_at_end(self, data):
        #Paso 1: Crear un nuevo nodo con el dato proporcionado
        new_node = Node(data)

        #Paso 2: Verificar si la lista está vacía
        if self.head is None and self.tail is None:
            #Si la lista está vacía, el nuevo nodo se convierte en la cabeza y la cola
            self.head = new_node
            self.tail = new_node
        else:
            #Si la lista no está vacía, el nodo actual de la cola apunta al nuevo nodo
            self.tail.next = new_node
            #Luego, la cola se actualiza para ser el nuevo nodo
            self.tail = new_node

    def search(self, data):
        #Paso 1: Iniciar un nodo temporal en la cabeza de la lista
        temp = self.head
        #Paso 2: Recorrer la lista mientras el nodo temporal no sea None
        while temp is not None:
            #Paso 3: Comparar el dato del nodo temporal con el dato buscado
            if temp.data == data:
                #Paso 4: Si se encuentra el dato, retornar True
                return True
            else:
                #Paso 5: Si no se encuentra el dato, avanzar al siguiente nodo
                temp = temp.next
        #Paso 6: Si se recorre toda la lista sin encontrar el dato, retornar False        
        return False