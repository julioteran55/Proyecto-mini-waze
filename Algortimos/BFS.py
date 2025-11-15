from collections import deque

def bfs(grafo, inicio, destino):
    """
    BFS para encontrar el camino con menos saltos entre dos nodos.
    No usa distancias, solo niveles.
    """

    # Verificar que los nodos existan
    inicio_vert = grafo.vertices.buscar(inicio)
    destino_vert = grafo.vertices.buscar(destino)

    if inicio_vert is None:
        print(f"El nodo {inicio} no existe en el grafo.")
        return None
    if destino_vert is None:
        print(f"El nodo {destino} no existe en el grafo.")
        return None

    # Estructuras de control
    visitados = set()
    padre = {}
    cola = deque()

    # Inicializar BFS
    cola.append(inicio)
    visitados.add(inicio)
    padre[inicio] = None

    # Bucle principal
    while cola:
        actual = cola.popleft()

        # Si llegamos al destino, reconstruimos el camino
        if actual == destino:
            break

        vertice_actual = grafo.vertices.buscar(actual)

        # recorrer las conexiones
        for arista in vertice_actual.conexiones:
            vecino = arista.destino

            if vecino not in visitados:
                visitados.add(vecino)
                padre[vecino] = actual
                cola.append(vecino)

    # Si el destino no fue visitado
    if destino not in visitados:
        print("No existe un camino entre esos nodos.")
        return None

    # Reconstruir el camino
    camino = []
    nodo = destino
    while nodo is not None:
        camino.insert(0, nodo)
        nodo = padre[nodo]

    return camino
