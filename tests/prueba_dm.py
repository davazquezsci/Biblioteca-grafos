from src.modelos import grafoDorogovtsevMendes

n = 200
g = grafoDorogovtsevMendes(n=n, dirigido=False)
g.to_graphviz("outputs/gv/dm_200.gv")

print("Nodos:", g.numero_nodos())
print("Aristas:", g.numero_aristas())
