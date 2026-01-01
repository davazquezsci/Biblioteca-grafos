from src.modelos import grafoGilbert

g = grafoGilbert(n=100, p=0.05, dirigido=False)
g.to_graphviz("outputs/gv/gilbert_100.gv")

print("Nodos:", g.numero_nodos())
print("Aristas:", g.numero_aristas())
