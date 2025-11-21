from Estructuras.MinHeap import MinHeap  #
from Eventos.eventos import obtener_distancia
def dijkstra(grafo, inicio, destino):

    # Validar existencia de nodos
    if grafo.vertices.buscar(inicio) is None:
        print(f"El nodo {inicio} no existe.")
        return None, None

    if grafo.vertices.buscar(destino) is None:
        print(f"El nodo {destino} no existe.")
        return None, None

    # === Inicialización ===
    distancias = {}
    padre = {}

    # Inicializamos distancias en +∞
    for nombre, vertice in grafo.vertices.items():
        distancias[nombre] = float("inf")
        padre[nombre] = None

    distancias[inicio] = 0

    # MinHeap: almacenará tuplas (distancia, nodo)
    heap = MinHeap()
    heap.insertar((0, inicio))

    visitados = set()

    # === Bucle principal usando MIN HEAP ===
    while not heap.esta_vacio():

        # extraemos el nodo con menor distancia
        dist_actual, actual = heap.extraer_min()

        # evitar procesar nodos repetidos
        if actual in visitados:
            continue

        visitados.add(actual)

        # si llegamos al destino, podemos terminar
        if actual == destino:
            break

        # obtener vértice real desde tabla hash
        vertice_obj = grafo.vertices.buscar(actual)

        # recorrer aristas (vecinos)
        for arista in vertice_obj.conexiones:
            vecino = arista.destino
            #antes
            #peso = arista.distanciaS
            peso = obtener_distancia(arista)
            nueva_dist = distancias[actual] + peso

            # RELAJACIÓN
            if nueva_dist < distancias[vecino]:
                distancias[vecino] = nueva_dist
                padre[vecino] = actual
                heap.insertar((nueva_dist, vecino))  # agregamos en heap

    # === Reconstrucción del camino ===
    if distancias[destino] == float("inf"):
        return None, None

    camino = []
    nodo = destino
    
    while nodo is not None:
        camino.insert(0, nodo)
        nodo = padre[nodo]

    return camino, distancias[destino]
