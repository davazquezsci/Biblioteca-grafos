from __future__ import annotations

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))




import math
import random
from typing import Optional, Tuple

from src.grafo import Grafo


def grafoMalla(m: int, n: int, dirigido: bool = False) -> Grafo:
    """
    Modelo Gm,n de malla.
    Crear m*n nodos. Para ni,j crear arista con ni+1,j y ni,j+1.
    """
    if m <= 1 or n <= 1:
        raise ValueError("m y n deben ser > 1")

    g = Grafo(dirigido=dirigido)

    # nodos con id (i, j)
    for i in range(m):
        for j in range(n):
            g.add_nodo((i, j))

    # aristas derecha y abajo
    for i in range(m):
        for j in range(n):
            if i + 1 < m:
                g.add_arista((i, j), (i + 1, j))
            if j + 1 < n:
                g.add_arista((i, j), (i, j + 1))

    return g


def grafoErdosRenyi(n: int, m: int, dirigido: bool = False, seed: Optional[int] = None) -> Grafo:
    """
    Modelo Gn,m de Erdös–Rényi: n nodos, elegir uniformemente m pares distintos.
    """
    if n <= 0:
        raise ValueError("n debe ser > 0")
    if m < 0:
        raise ValueError("m debe ser >= 0")

    rng = random.Random(seed)

    # máximo de aristas posibles sin loops
    max_edges = n * (n - 1) if dirigido else (n * (n - 1)) // 2
    if m > max_edges:
        raise ValueError(f"m es demasiado grande. Máximo posible: {max_edges}")

    g = Grafo(dirigido=dirigido)
    for i in range(n):
        g.add_nodo(i)

    # generar todas las posibles y samplear m sin repetición
    # (para n=500, no dirigido => ~124,750 posibles; es manejable)
    posibles = []
    if dirigido:
        for u in range(n):
            for v in range(n):
                if u != v:
                    posibles.append((u, v))
    else:
        for u in range(n):
            for v in range(u + 1, n):
                posibles.append((u, v))

    elegidas = rng.sample(posibles, m)
    for u, v in elegidas:
        g.add_arista(u, v)

    return g


def grafoGilbert(n: int, p: float, dirigido: bool = False, seed: Optional[int] = None) -> Grafo:
    """
    Modelo Gn,p de Gilbert: para cada par, crear arista con probabilidad p.
    """
    if n <= 0:
        raise ValueError("n debe ser > 0")
    if not (0.0 < p < 1.0):
        raise ValueError("p debe estar en (0, 1)")

    rng = random.Random(seed)

    g = Grafo(dirigido=dirigido)
    for i in range(n):
        g.add_nodo(i)

    if dirigido:
        for u in range(n):
            for v in range(n):
                if u != v and rng.random() < p:
                    g.add_arista(u, v)
    else:
        for u in range(n):
            for v in range(u + 1, n):
                if rng.random() < p:
                    g.add_arista(u, v)

    return g


def grafoGeografico(n: int, r: float, dirigido: bool = False, seed: Optional[int] = None) -> Grafo:
    """
    Modelo Gn,r geográfico simple: nodos en [0,1]x[0,1] y conectar si dist <= r.
    """
    if n <= 0:
        raise ValueError("n debe ser > 0")
    if not (0.0 < r < 1.0):
        raise ValueError("r debe estar en (0, 1)")

    rng = random.Random(seed)

    g = Grafo(dirigido=dirigido)

    coords = {}
    for i in range(n):
        x = rng.random()
        y = rng.random()
        g.add_nodo(i, x=x, y=y)
        coords[i] = (x, y)

    # conectar por distancia (euclidiana)
    r2 = r * r
    if dirigido:
        for u in range(n):
            xu, yu = coords[u]
            for v in range(n):
                if u == v:
                    continue
                xv, yv = coords[v]
                dx = xu - xv
                dy = yu - yv
                if dx * dx + dy * dy <= r2:
                    g.add_arista(u, v)
    else:
        for u in range(n):
            xu, yu = coords[u]
            for v in range(u + 1, n):
                xv, yv = coords[v]
                dx = xu - xv
                dy = yu - yv
                if dx * dx + dy * dy <= r2:
                    g.add_arista(u, v)

    return g


def grafoBarabasiAlbert(n: int, d: int, dirigido: bool = False, seed: Optional[int] = None) -> Grafo:
    """
    Variante Gn,d Barabási–Albert:
    - Los primeros d nodos forman un clique (todos con todos).
    - Cada nodo nuevo se conecta a d nodos distintos, con prob ∝ grado actual.
    """
    if n <= 0:
        raise ValueError("n debe ser > 0")
    if d <= 1:
        raise ValueError("d debe ser > 1")
    if d >= n:
        raise ValueError("d debe ser < n")

    rng = random.Random(seed)
    g = Grafo(dirigido=dirigido)

    for i in range(n):
        g.add_nodo(i)

    # clique inicial entre 0..d-1
    for u in range(d):
        for v in range(u + 1, d):
            g.add_arista(u, v)

    # "bolsa" para muestreo proporcional al grado
    # cada nodo aparece tantas veces como su grado (aprox)
    bag = []
    for u in range(d):
        deg = g.grado(u)
        bag.extend([u] * max(1, deg))  # mínimo 1 para no dejar nodos fuera

    for new_node in range(d, n):
        targets = set()
        # elegir d distintos
        while len(targets) < d:
            if not bag:
                # caso raro: si bag está vacía, elegir uniforme
                cand = rng.randrange(0, new_node)
            else:
                cand = rng.choice(bag)
            if cand != new_node:
                targets.add(cand)

        for t in targets:
            g.add_arista(new_node, t)

        # actualizar bag: el nuevo nodo entra con grado d, y cada target sube grado +1
        bag.extend([new_node] * max(1, g.grado(new_node)))
        for t in targets:
            bag.append(t)

    return g




def grafoDorogovtsevMendes(n: int, dirigido: bool = False, seed: Optional[int] = None) -> Grafo:
    """
    Modelo Gn Dorogovtsev–Mendes:
    - Iniciar con triángulo (3 nodos, 3 aristas).
    - Cada nodo nuevo: seleccionar una arista al azar (u,v) y conectar nuevo con u y v.
    """
    if n < 3:
        raise ValueError("n debe ser >= 3")

    rng = random.Random(seed)
    g = Grafo(dirigido=dirigido)

    for i in range(n):
        g.add_nodo(i)

    # triángulo inicial
    g.add_arista(0, 1)
    g.add_arista(1, 2)
    g.add_arista(2, 0)

    # lista de aristas como pares (u_id, v_id)
    # en no dirigido guardamos (min,max) para normalizar
    def norm(u, v):
        return (u, v) if dirigido else ((u, v) if u < v else (v, u))

    edge_list = [norm(0, 1), norm(1, 2), norm(0, 2)]

    for new_node in range(3, n):
        u, v = rng.choice(edge_list)

        g.add_arista(new_node, u)
        g.add_arista(new_node, v)

        edge_list.append(norm(new_node, u))
        edge_list.append(norm(new_node, v))

    return g
