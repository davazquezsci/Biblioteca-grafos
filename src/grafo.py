
    
class Nodo:
    """
    Representa un nodo (vértice) del grafo.
    """

    def __init__(self, id, x=None, y=None):
        self.id = id
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Nodo({self.id})"

    def __eq__(self, other):
        if not isinstance(other, Nodo):
            return False
        return self.id == other.id

    def __hash__(self):
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
    



