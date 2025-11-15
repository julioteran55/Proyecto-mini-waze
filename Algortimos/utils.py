
def reconstruir_camino(padre, destino):
    if destino not in padre:
        return None

    camino = []
    nodo = destino
    while nodo is not None:
        camino.insert(0, nodo)
        nodo = padre[nodo]

    return camino

