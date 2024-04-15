from libro import Libro

class Nodo:
    #Constructor de la clse nodo
    def __init__(self, id, titulo, autor):
        self.libro = Libro(id, titulo, autor)
        self.right =  None 
        self.left = None
        self.level = -1
    #Información en string de cada recurso
    def __str__(self):
        return f'\nInfo del recurso: \nID: {self.libro.id}. Título: {self.libro.titulo}. Autor: {self.libro.autor}. Estado de préstamo: {self.libro.estado}. '