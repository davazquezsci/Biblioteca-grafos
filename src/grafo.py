
    
class Nodo:
    """
    Representa un nodo (vértice) del grafo.
    """
    #Contructor
    def __init__(self, id, x=None, y=None):
        self.id = id
        self.x = x
        self.y = y

    #Representacion legible ( solo muestra como se ve el nodo )
    def __repr__(self):
        return f"Nodo({self.id})"

    def __eq__(self, other):
        if not isinstance(other, Nodo): #isinstance  devuelve True si other es de la clase Nodo y False si no 
            return False
        return self.id == other.id

    def __hash__(self): #Define la Huella digital de cada  Nodo 
        return hash(self.id)


class Arista:
    """
    Representa una arista entre dos nodos.
    Puede ser dirigida o no dirigida (el grafo decide).
    """

    def __init__(self, origen: Nodo, destino: Nodo):
        if origen == destino:
            raise ValueError("No se permiten aristas de un nodo a sí mismo")

        self.origen = origen
        self.destino = destino

    def __repr__(self) -> str:
        return f"Arista({self.origen.id} -> {self.destino.id})"  
    



