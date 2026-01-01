from src.modelos import grafoGeografico

g = grafoGeografico(n=200, r=0.12, dirigido=False)
g.to_graphviz("outputs/gv/geografico_200.gv")

print("Nodos:", g.numero_nodos())
print("Aristas:", g.numero_aristas())
