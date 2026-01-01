from src.modelos import grafoBarabasiAlbert

n = 200
d = 3  # número de conexiones por nodo nuevo

g = grafoBarabasiAlbert(n=n, d=d, dirigido=False)
g.to_graphviz("outputs/gv/barabasi_albert_200.gv")

print("Nodos:", g.numero_nodos())
print("Aristas:", g.numero_aristas())
