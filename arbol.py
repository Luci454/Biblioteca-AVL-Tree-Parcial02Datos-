from Nodo import Nodo
from listaAux import ListaAux
class Arbol:
    #Constructor del arbol
    def __init__(self):
        self.root = None

    # Imprimir el árbol
    def printTree(self):
        self.printTreeRec(self.root, 0)
    
    def printTreeRec(self, nodo, level):
        if nodo is not None:
            self.printTreeRec(nodo.right, level + 1)
            for _ in range(level):
                print("  ", end="")
            print(nodo.libro.id)
            self.printTreeRec(nodo.left, level + 1)

    #Búsqueda por ID
    def search(self, nodo, valor):
        if nodo is None:
            return None
        elif nodo.libro.id == valor:  #Encontro el nodo con el ID correcto
            return nodo
        elif valor > nodo.libro.id:
            return self.search(nodo.right, valor) #Si e ID es mayor al del nodo actual, repetir el proceso con el nodo hijo derecho
        elif valor < nodo.libro.id:
            return self.search(nodo.left, valor) #Si e ID es menor al del nodo actual, repetir el proceso con el nodo hijo izquierdo

    def searchBoolean(self, nodo, valor):
        if nodo is None:
            return False
        elif nodo.libro.id == valor:
            return True
        elif valor > nodo.libro.id:
            return self.search(nodo.right, valor)
        elif valor < nodo.libro.id:
            return self.search(nodo.left, valor)

    #Prestar un libro
    def prestar(self, valor, lista):
        libroPrestar = self.search(self.root, valor) #Busca el ID en la biblioteca para prestar el libro

        if libroPrestar is not None and libroPrestar.libro.estado == "disponible": #Si está disponible el recurso, puede prestarlo
            libroPrestar.libro.estado = "prestado"
            lista.prestarFromLista(valor) # Repeir en la estructura auxiliar
            print(f'\nSe ha prestado exitosamente el libro {libroPrestar.libro.titulo}.')
        else:
            print("\nEl libro no está disponible.")

    #Cambiar la disponibilidad de los recursos
    def cambiarDisponibilidad(self, valor, estadoLibro, lista):
        libroACambiar = self.search(self.root, valor) #Busca el ID en la biblioteca para modificar el estado de disponibilidad el libro.
        
        estadoLibro = estadoLibro.lower()
        if libroACambiar is not None and libroACambiar.libro.estado == "disponible" and estadoLibro == "prestado": #Si está disponible el recurso, puede prestarlo
            libroACambiar.libro.estado = estadoLibro
            lista.actualizarEstado(valor, estadoLibro)
            print("\nHa cambiado exitosamente el estado del libro.")
        elif libroACambiar is not None and libroACambiar.libro.estado == "prestado" and estadoLibro == "disponible": #Si está prestado el recurso, puede cambialo a disponible
            libroACambiar.libro.estado = estadoLibro
            lista.actualizarEstado(valor, estadoLibro)
            print("\nHa cambiado exitosamente el estado del libro.")
        else:
            print("\nEl estado por el cual desea modificar la condición actual del libro es inválido o el libro no se encuentra disponible.")

    # Método para eliminar un recurso de biblioteca. Como parametros recibe un valor (id) y la lista auxiliar
    def deleteNode(self, valor, lista):
        if self.searchBoolean(self.root, valor): # Verificamos si el libro con el id (valor) digitado existe (usamos el método searchBoolean)
            lista.eraseFromLista(valor) # Si existe, entonces se elimina de la lista pasándole el valor (id)
            return self.deleteNodeRec(self.root, valor) # Retornamos lo que retorne el método recursivo deleteNodeRec (elimina el nodo con el id digitado del árbol)
        else:
            return None# Si no existe, retornamos None

    # Método recursivo para eliminar un nodo de un árbol. Como parámetros recibe un nodo "actual" y un valor a buscar (el id del libro a eliminar)
    def deleteNodeRec(self, nodo, valor):
        if nodo is None:  # Revisamos si el nodo es None
            return None # Retornamos None si el nodo es None
    
        elif nodo.libro.id < valor: # Revisamos si el id del nodo en el que estamos es menor que el id (valor) que se pasó

            # Le asignamos al apuntador de la derecha lo que retorne el llamado recursivo del método al cual se le pasa el nodo a la derecha del "actual" y el mismo id (valor)
            nodo.right = self.deleteNodeRec(nodo.right, valor)
        
        elif nodo.libro.id > valor: # Revisamos si el id del nodo en el que estamos es mayor que el id (valor) que se pasó

            # Le asignamos al apuntador de la izquierda lo que retorne el llamado recursivo del método al cual se le pasa el nodo a la izquierda del "actual" y el mismo id (valor)
            nodo.left = self.deleteNodeRec(nodo.left, valor)
        
        elif nodo.right is None: # Revisamos si el nodo a la derecha del "actual" es None

            return nodo.left # Si el nodo a la derecha del "actual" es None, retornamos el nodo a la izquierda del "actual"
        
        elif nodo.left is None: # Revisamos si el nodo a la izquierda del "actual" es None

            return nodo.right  # Si el nodo a la izquierda del "actual" es None, retornamos el nodo a la derecha del "actual"
        
        else: # Revisamos el caso en el que estemos en el nodo a eliminar y tenga los dos nodos "hijos" no vacíos

            # Vamos a buscar el sucesor más proximo al id que tenemos que eliminar

            # Llevamos una variable de control que empiece en el nodo de la derecha del actual
            control = nodo.right

            # Ciclo while que itera mientras el nodo de la izquierda de la variable de control no sea None
            while control.left is not None:

                # Actualiza la variable de control, convirtiéndose en el nodo izquierdo del nodo que era control
                control = control.left
            
            # Al encontrar el sucesor más próximo, se copia el libro de este en el nodo con el id que se iba a eliminar
            nodo.libro = control.libro
            
            # Se hace un llamado recursivo del método para eliminar el libro "duplicado"
            # por ello se le pasa el id del libro del nodo control y se empieza en la derecha para que no borre el nodo en el que se copió la información
            nodo.right = self.deleteNodeRec(nodo.right, control.libro.id)
        
        # Se retorna nodo actual para poder mantener la "integridad" del árbol
        return nodo
        

    def rotationLL(self, node):
        newRoot = node.left
        node.left = newRoot.right
        newRoot.right = node

        newRoot.level = newRoot.level - 1

        node.level = node.level + 1
        if node.right is not None:
            node.right.level = node.right.level + 1

        aux = newRoot.left
        aux.level = aux.level - 1
        if aux.left is not None:
            aux.left.level = aux.left.level  - 1

        if aux.right is not None:
            aux.right.level = aux.right.level  - 1

        return newRoot

    def rotationRR(self, node):
        newRoot = node.right
        node.right= newRoot.left
        newRoot.left = node
        
        newRoot.level = newRoot.level - 1

        node.level = node.level + 1
        if node.left is not None:
            node.left.level = node.left.level + 1

        aux = newRoot.right
        if aux is not None:
            aux.level = aux.level - 1
            if aux.right is not None:
                aux.right.level = aux.right.level - 1
            if aux.left is not None:
                aux.left.level = aux.right.level  - 1

        return newRoot

    def rotationRL(self, nodo):
        if nodo is not None and nodo.right is not None:
            temp = nodo.right
            nodo.right = temp.left
            if nodo.right is not None:
                temp.left = nodo.right.right
                nodo.right.right = temp

                nodo.right.level -= 1
                if nodo.right.left is not None:
                    nodo.right.left.level -= 1
                
                temp.level += 1
                if temp.right is not None:
                    temp.right.level += 1

                return self.rotationRR(nodo)  # *
        # return nodo

    def rotationLR(self, nodo):
        temp = nodo.left
        nodo.left = temp.right
        temp.right = nodo.left.left
        nodo.left.left = temp

        nodo.left.level -= 1
        if nodo.left.right is not None:
            nodo.left.right.level -= 1
        
        temp.level += 1
        if temp.left is not None:
            temp.left.level += 1

        return self.rotationLL(nodo) # *

    def calcularNivel(self, nodo):
        if nodo is None:
            return 0
        else:
            if nodo.left is None and nodo.right is None:
                return 1  # Si el nodo no tiene hijos, su altura es 1
            else:
                # Calculamos la altura máxima entre el subárbol izquierdo y derecho,
                # y sumamos 1 para contar el nivel actual
                return max(self.calcularNivel(nodo.left), self.calcularNivel(nodo.right)) + 1


    def buscarNodoNB(self, nodo):
        nivelIzq = self.calcularNivel(nodo.left)
        nivelDer = self.calcularNivel(nodo.right)

        if nivelDer - nivelIzq == 2 or nivelIzq - nivelDer == 2:
            return True
        else:
            return False

    def identifyRRorRL(self, nodo):
        nivelIzq = self.calcularNivel(nodo.right.left)
        nivelDer = self.calcularNivel(nodo.right.right)

        if nivelDer > nivelIzq:
            return self.rotationRR(nodo)
        else:
            return self.rotationRL(nodo)

    def identifyLLorLR(self, nodo):
        nivelIzq = self.calcularNivel(nodo.left.left)
        nivelDer = self.calcularNivel(nodo.left.right)

        if nivelIzq > nivelDer:
            return self.rotationLL(nodo)
        else:
            return self.rotationLR(nodo)

    def balancearArbol(self, nodo):
        if nodo is None:
            pass
        elif nodo is self.root and self.buscarNodoNB(self.root):
            nivelIzq = self.calcularNivel(nodo.left)
            nivelDer = self.calcularNivel(nodo.right)

            if nivelIzq > nivelDer:
                self.root = self.identifyLLorLR(self.root) 
            else:
                self.root = self.identifyRRorRL(self.root)
                
        elif nodo.right is not None:
            if self.buscarNodoNB(nodo.right):
                nodo.right = self.identifyRRorRL(nodo.right)
            else:
                self.balancearArbol(nodo.right)
        elif nodo.left is not None:
            if self.buscarNodoNB(nodo.left):
                nodo.left = self.identifyLLorLR(nodo.left)
            else:
                self.balancearArbol(nodo.left)

    def canBeBalanced(self):
        nivelIzq = self.calcularNivel(self.root.left)
        nivelDer = self.calcularNivel(self.root.right)

        if nivelIzq > 1 or nivelDer > 1:
            return True
        else:
            return False
        
    
    # Método recursivo para inserción del libro nuevo en el árbol. Recibe como parámetro el nodo "actual", el nodo a añadir y el nivel "actual"
    def insertRecurtion(self, nodo, newNode, level):

        # Se revisa si el id del nuevo nodo es mayor que el id del nodo "actual" y si el nodo derecho del nodo "actual" es vacío
        if newNode.libro.id > nodo.libro.id and nodo.right is None:

            # El nivel del nuevo nodo se convierte en el nivel siguiente del que estamos
            newNode.level = level + 1

            # El apuntador de la derecha del nodo "actual" apunta al nuevo nodo
            nodo.right = newNode
            print("\nSe ha insertado el libro exitosamente")

            # Se revisa si es posible que el arbol esté desbalanceado y se pueda balancear
            if self.canBeBalanced():

                # Se invoca el método para balancear el árbol empezando en la raíz
                self.balancearArbol(self.root)
        
        # Se revisa si el id del nuevo nodo es menor que el id del nodo "actual" y si el nodo izquierdo del nodo "actual" es vacío
        elif newNode.libro.id < nodo.libro.id and nodo.left is None:

            # El nivel del nuevo nodo se convierte en el nivel siguiente del que estamos
            newNode.level = level + 1

            # El apuntador de la izquierda del nodo "actual" apunta al nuevo nodo
            nodo.left = newNode
            print("\nSe ha insertado el libro exitosamente")

            # Se revisa si es posible que el arbol esté desbalanceado y se pueda balancear
            if self.canBeBalanced():

                # Se invoca el método para balancear el árbol empezando en la raíz
                self.balancearArbol(self.root)

        # Se revisa si el id del nuevo nodo es mayor que el id del nodo "actual"
        elif newNode.libro.id > nodo.libro.id:

            # Se invoca el método recursivamente pero ahora con el nodo de la derecha y sumándole un nivel
            self.insertRecurtion(nodo.right, newNode, level + 1)

        # Se revisa si el id del nuevo nodo es menor que el id del nodo "actual"
        elif newNode.libro.id < nodo.libro.id:

            # Se invoca el método recursivamente pero ahora con el nodo de la izquierda y sumándole un nivel
            self.insertRecurtion(nodo.left, newNode, level + 1)
        else:
            # En el else se llega a la conclusión de que el id del nuevo nodo y el nodo actual son iguales
            print("\nYa hay un libro con el mismo ID")


    # Método de inserción en el arbol y lista auxiliar. Pasamos como parámetros los datos del libro y la lista auxiliar
    def insert(self, id, titulo, autor, listaAux):

        # Inicializamos indicador de un libro existente con el mismo ID en falso
        sameID = False

        # For-each para recorrer la lista auxiliar
        for item in listaAux.lista:

            # Vemos si alguno de los id de los items en la lista coincide con el id pasado
            if item.id == id:

                # Actualizamos la bandera en true si encontramos un id existente igual
                sameID = True

        # Condicional que revisa si no se encontró alguna coincidencia
        if not sameID:

            # Si no se tiene algún elemento con el mismo id, se añade el libro a la lista
            listaAux.insertInLista(id, titulo, autor)

        # Se crea un nuevo nodo con los datos del libro
        newNode = Nodo(id, titulo, autor)

        # Se revisa si la raíz es vacía
        if self.root is None:

            # Si la raíz es vacía, la raíz apuntará al nuevo nodo
            self.root = newNode
            print("\nSe ha insertado el libro exitosamente")
        else:

            # Si hay una raíz, se invoca el método recursivo que recibe la raíz, el nuevo nodo y el nivel 0
            self.insertRecurtion(self.root, newNode, 0)

    #Imprimir la información de los nodos del árbol en preorder
    def preorderTraversal(self, node):
        if node:
            print(node)                
            self.preorderTraversal(node.left)
            self.preorderTraversal(node.right)
