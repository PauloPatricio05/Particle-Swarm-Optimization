# Contém Sphere, Rastrigin e Rosenbrock

import math

def sphere(x):
    """Soma dos quadrados de cada elemento da lista"""
    total = 0
    for valor in x:
        total += valor ** 2
    return total

def rastrigin(x):
    """Fórmula com cosseno para gerar vários mínimos locais"""
    n = len(x)
    total = 0
    for valor in x:
        total += (valor ** 2 - 10 * math.cos(2 * math.pi * valor))
    return 10 * n + total

def rosenbrock(x):
    """Fórmula do vale de Rosenbrock"""
    total = 0
    # O loop vai até n-1 porque a fórmula usa o elemento atual e o próximo (i+1)
    for i in range(len(x) - 1):
        termo1 = 100 * (x[i+1] - x[i]**2)**2
        termo2 = (1 - x[i])**2
        total += termo1 + termo2
    return total