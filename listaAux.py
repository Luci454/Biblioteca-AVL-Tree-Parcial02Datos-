from libro import Libro
class ListaAux:
    
    def __init__(self):
        self.lista = [] 

    #Crear un libro en la lista
    def insertInLista(self, id, titulo, autor):   
        self.lista.append(Libro(id, titulo, autor))

    #Eliminar un libro en la lista
    def eraseFromLista(self, id):  
        for i in range (len(self.lista)):
            if self.lista[i].id == id:
                self.lista.remove(self.lista[i])
                break

    #Prestar un libro en la lista            
    def prestarFromLista(self, id):
        for i in range(len(self.lista)):
            if self.lista[i].id is id:
               self.lista[i].estado  =  "prestado"
               break

    #Actualizar un estado de disponibilidad de un libro en la lista        
    def actualizarEstado (self, id, estado):
        for i in range (len(self.lista)):
            if self.lista[i].id == id:
                self.lista[i].estado = estado
    
    #Buscar un libro por título en la lista e imprimir la información
    def buscarPorTitulo (self, titulo):
        bandera = False
        for i in range (len(self.lista)):
            if self.lista[i].titulo.lower() == titulo.lower():
                print(f'\nEl libro que busca se encuentra con el ID: {self.lista[i].id}. Autor: {self.lista[i].autor}. Estado: {self.lista[i].estado}.')
                bandera = True
                break    
        
        if bandera is False:
            print("\nEl libro que busca no se encuentra registrado en la biblioteca.")

    #Buscar autores en la lista e imprimir la información de los recursos que coincidan
    def buscarAutor (self, autor):
        bandera = False
        for i in range (len(self.lista)):
            if self.lista[i].autor.lower() == autor.lower():
                print(f'\nSe ha encontrado el autor en la obra: {self.lista[i].titulo}. ID: {self.lista[i].id}. Estado: {self.lista[i].estado}.')
                bandera = True

        if bandera is False:
            print("\nEl autor que busca no se encuentra registrado en la biblioteca.")

    #Buscar rescursos con cierto estado de disponibilidad e imprimir la información de los que coinciden
    def buscarEstados (self, estado):
        bandera = False
        estado = estado.lower()   
        print("\nA continuación verá los recursos existentes que coinciden con el estado de su búsqueda.")

        for i in range (len(self.lista)):
            if self.lista[i].estado == estado:
                print(f'\nTitulo: {self.lista[i].titulo}. ID: {self.lista[i].id}.')
                bandera = True    

        if bandera is False:
            print("\nParece que no hay recursos existentes que coinciden con el estado de su búsqueda.")