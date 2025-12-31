import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.grafo import Grafo

g = Grafo(dirigido=False)
g.add_nodo("A")
g.add_nodo("B")
g.add_nodo("C")

g.add_arista("A", "B")
g.add_arista("B", "C")
g.add_arista("C", "A")

g.to_graphviz("outputs/gv/prueba.gv")
print("Nodos:", g.numero_nodos())
print("Aristas:", g.numero_aristas())
