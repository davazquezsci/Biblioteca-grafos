from src.modelos import grafoErdosRenyi

g = grafoErdosRenyi(n=100, m=300, dirigido=False)
g.to_graphviz("outputs/gv/erdos_renyi_100.gv")

print("Nodos:", g.numero_nodos())
print("Aristas:", g.numero_aristas())
