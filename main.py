from arbol import Arbol
from listaAux import ListaAux

def menu():
    #Crear los libros en la biblioteca (árbol AVL)
    biblioteca = Arbol()
    lista_aux = ListaAux()
    biblioteca.insert(1, "El amor en los tiempos del cólera", "Gabriel Garcia Marquez", lista_aux)
    biblioteca.insert(2, "Sentido y sensibilidad", "Jane Austen", lista_aux)
    biblioteca.insert(3, "Una corte de rosas y espinas", "Sara J. Mass", lista_aux)
    biblioteca.insert(4, "Dracula", "Bram Stoker", lista_aux)
    biblioteca.insert(5, "Frankestein", "Mary Shelley", lista_aux)


    while True:
        #Imprimir la opciones del menú
        print("\n\nMenú:")
        print("1 Reporte de los libros de la biblioteca en Pre-order.")
        print("2 Agregar un libro nuevo a la biblioteca.")
        print("3 Eliminar un libro por ID (Debe ingresar ID).")
        print("4 Actualizar el estado de un libro en Prestado o Disponible (Debe ingresar ID).")
        print("5 Buscar un libro por ID (Debe ingresar ID).")
        print("6 Buscar un libro por título.")
        print("7 Buscar recursos por nombre de autor.")
        print("8 Buscar recursos por estado de préstamo.")
        print("9 Prestar un libro (Debe ingresar ID)")
        print("10. Salir")
        op = input("\nDigite una opción: ")

        if op == "1":
            print("\nBiblioteca de libros en preorder por ID:") 
            biblioteca.preorderTraversal(biblioteca.root) 
            print("\nÁrbol de la bilbioteca actual:") #Imprimir el árbol de la biblioteca con los ID de los recursos
            biblioteca.printTree()

        elif op == "2":
            try:
                libroId = int(input("\nIngrese el ID del libro: "))
                titulo = input("\nIngrese el título del libro: ")
                autor = input("\nIngrese el autor del libro: ")
                biblioteca.insert(libroId, titulo, autor, lista_aux)
            except Exception as e:
                print("\nValor de ID ingresado inválido.")    

        elif op == "3":
            try:    
                id = int(input("\nIngrese el id del libro que desea eliminar: "))
                if id == biblioteca.root.libro.id and biblioteca.root.right is None and biblioteca.root.left is None:
                    biblioteca.root = None
                    print("\nEl libro fue eliminado exitosamente.")
                else:
                    aux = biblioteca.deleteNode(id, lista_aux)
                    if aux is not None:
                        biblioteca.root = aux
                        print("\nEl libro fue eliminado exitosamente.")
                        if biblioteca.canBeBalanced():
                            biblioteca.balancearArbol(biblioteca.root)
                    else:
                        print("\nEl libro no pudo ser eliminado ya que no se encuentra en la biblioteca.")
            except Exception as e:
                print("\nValor de ID ingresado inválido.")  

        elif op == "4":
            try:
                id = int(input("\nIngrese el id del libro cuyo estado modificará: "))
                estadoLibro = input("\nIngrese el estado que desea ponerle al recurso: ")
                biblioteca.cambiarDisponibilidad(id, estadoLibro, lista_aux)
            except Exception as e:
                print("\nValor de ID ingresado inválido.")  

        elif op == "5": 
            try:    
                id = int(input("\nIngrese el id del libro que desea buscar: "))
                result = biblioteca.search(biblioteca.root, id)
                if result is None:
                    print("\nEl libro que busca no está en la biblioteca.")
                else:
                    print(result)
            except Exception as e:
                print("\nValor de ID ingresado inválido.")  

        elif op == "6":
            titulo = input("\nIngrese el título del libro que busca: ")
            lista_aux.buscarPorTitulo(titulo)

        elif op == "7":
            autor = input("\nIngrese el nombre del autor que busca: ")
            lista_aux.buscarAutor(autor)
        
        elif op == "8":
            estado = input("\nIngrese el estado de préstamo que desea buscar: ")
            lista_aux.buscarEstados(estado)

        elif op== "9":
            try: 
                id = int(input("Ingrese el ID del libro que desea prestar: "))
                biblioteca.prestar(id, lista_aux)
            except Exception as e:
                print("\nValor de ID ingresado inválido.")
                
        elif op == "10":
            print("\n¡Gracias por usar el sistema de la biblioteca de Luciana!")
            break
        else:
            print("\nOpción de menú inválida.")
            

if __name__ == '__main__':
    print("\n¡Bienvenid@ al sistema de la biblioteca de Luciana!")
    menu()

    