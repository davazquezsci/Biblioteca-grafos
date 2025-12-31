
    
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


   
    
class Grafo:
    """
    Grafo dirigido o no dirigido.
    - Guarda nodos por id
    - Evita aristas duplicadas
    - Mantiene lista de adyacencia para grados y recorridos
    """ 
    """
    A grandes razgos lo que queremos computaciónalmente es  
    - almacenar nodos
    - almacenar aristas 
    - evitar duplicados 
    - saber quien esta conectado con quien 
    - exportarlo a GraphViz 
    ç
    
    """

    def __init__(self, dirigido: bool = False):
        self.dirigido = dirigido

        # nodos: id -> Nodo 
        '''
        Creamos un diccionario de  todos los nodos del grafo ( Conjunto Grafo) con su identificador 
        '''
        self._nodos = {}

        # adyacencia: Nodo -> set(Nodo)
        '''
        Creamos un diccionario de  todos los nodos del grafo que estan conectados a un nodo especifico 
        '''
        self._ady = {}

        # conjunto de claves de aristas para evitar duplicados
        # dirigido: (u_id, v_id)
        # no dirigido: (min(u_id,v_id), max(u_id,v_id))
        self._aristas_key = set()

        # lista explícita de Arista (opcional pero útil)
        self._aristas = []

    def add_nodo(self, id, x=None, y=None) -> Nodo:
        if id in self._nodos:
            return self._nodos[id]

        nodo = Nodo(id, x=x, y=y)
        self._nodos[id] = nodo
        self._ady[nodo] = set()
        return nodo

    def get_nodo(self, id) -> Nodo:
        return self._nodos[id]

    def nodos(self):
        return list(self._nodos.values())

    def aristas(self):
        return list(self._aristas)

    def _key_arista(self, u: Nodo, v: Nodo):
        if self.dirigido:
            return (u.id, v.id)
        a, b = u.id, v.id
        return (a, b) if a <= b else (b, a)

    def add_arista(self, u_id, v_id) -> bool:
        """
        Agrega arista entre u y v.
        Retorna True si se agregó, False si ya existía.
        """
        if u_id == v_id:
            raise ValueError("No se permiten aristas de un nodo a sí mismo")

        if u_id not in self._nodos or v_id not in self._nodos:
            raise KeyError("Ambos nodos deben existir antes de crear una arista")

        u = self._nodos[u_id]
        v = self._nodos[v_id]

        key = self._key_arista(u, v)
        if key in self._aristas_key:
            return False  # duplicada

        # registrar
        self._aristas_key.add(key)
        self._aristas.append(Arista(u, v))

        # adyacencia
        self._ady[u].add(v)
        if not self.dirigido:
            self._ady[v].add(u)

        return True

    def vecinos(self, id):
        n = self._nodos[id]
        return set(self._ady[n])

    def grado(self, id) -> int:
        n = self._nodos[id]
        return len(self._ady[n])

    def numero_nodos(self) -> int:
        return len(self._nodos)

    def numero_aristas(self) -> int:
        return len(self._aristas_key)

    def to_graphviz(self, path: str):
        """
        Guarda el grafo en formato GraphViz simple (.gv).
        """
        if self.dirigido:
            header = "digraph G {"
            sep = "->"
        else:
            header = "graph G {"
            sep = "--"

        lines = [header]

        # declarar nodos (por si hay nodos aislados)
        for nodo in self.nodos():
            # opcional: incluir pos si tiene coordenadas
            if nodo.x is not None and nodo.y is not None:
                lines.append(f'  "{nodo.id}" [pos="{nodo.x},{nodo.y}!"];')
            else:
                lines.append(f'  "{nodo.id}";')

        # declarar aristas
        for (a, b) in self._aristas_key:
            lines.append(f'  "{a}" {sep} "{b}";')

        lines.append("}")

        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))



