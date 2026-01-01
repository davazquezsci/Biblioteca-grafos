from src.modelos import (
    grafoMalla,
    grafoGilbert,
    grafoErdosRenyi,
    grafoGeografico,
    grafoDorogovtsevMendes,
    grafoBarabasiAlbert,
)

import math
import os

BASE = "outputs/gv"

def ensure(path):
    os.makedirs(path, exist_ok=True)

sizes = [50, 200, 500]

# ---------- MALLA ----------
ensure(f"{BASE}/malla")
for n in sizes:
    m = int(math.sqrt(n))
    g = grafoMalla(m, n // m)
    g.to_graphviz(f"{BASE}/malla/malla_{n}.gv")

# ---------- GILBERT ----------
ensure(f"{BASE}/gilbert")
for n in sizes:
    g = grafoGilbert(n=n, p=0.05)
    g.to_graphviz(f"{BASE}/gilbert/gilbert_{n}.gv")

# ---------- ERDOS-RENYI ----------
ensure(f"{BASE}/erdos_renyi")
for n in sizes:
    m = int(0.05 * (n * (n - 1) / 2))
    g = grafoErdosRenyi(n=n, m=m)
    g.to_graphviz(f"{BASE}/erdos_renyi/erdos_renyi_{n}.gv")

# ---------- GEOGRAFICO ----------
ensure(f"{BASE}/geografico")
for n in sizes:
    g = grafoGeografico(n=n, r=0.12)
    g.to_graphviz(f"{BASE}/geografico/geografico_{n}.gv")

# ---------- DOROGOVTSEV-MENDES ----------
ensure(f"{BASE}/dorogovtsev_mendes")
for n in sizes:
    g = grafoDorogovtsevMendes(n=n)
    g.to_graphviz(f"{BASE}/dorogovtsev_mendes/dm_{n}.gv")

# ---------- BARABASI-ALBERT ----------
ensure(f"{BASE}/barabasi_albert")
for n in sizes:
    g = grafoBarabasiAlbert(n=n, d=3)
    g.to_graphviz(f"{BASE}/barabasi_albert/ba_{n}.gv")
