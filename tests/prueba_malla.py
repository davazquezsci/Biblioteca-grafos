from src.modelos import grafoMalla

g = grafoMalla(10, 10, dirigido=False)  # 100 nodos
g.to_graphviz("outputs/gv/malla_100.gv")

print("Nodos:", g.numero_nodos())
print("Aristas:", g.numero_aristas())
 
