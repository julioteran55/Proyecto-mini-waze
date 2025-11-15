def dijkstra(grafo, inicio, destino):

    # 1. Verificar que los nodos existan
    if grafo.vertices.buscar(inicio) is None:
        print(f"El nodo {inicio} no existe en el grafo.")
        return None, None

    if grafo.vertices.buscar(destino) is None:
        print(f"El nodo {destino} no existe en el grafo.")
        return None, None

    # 2. Inicializar distancias y padres
    distancias = {}
    padre = {}

    for nombre, nodo in grafo.vertices.items():
        distancias[nombre] = float("inf")
        padre[nombre] = None

    distancias[inicio] = 0

    # 3. Crear conjunto de visitados
    visitados = set()

    # 4. Bucle principal
    while True:

        # Elegir el nodo no visitado con menor distancia
        actual = None
        menor_dist = float("inf")

        for nombre in distancias:
            if nombre not in visitados and distancias[nombre] < menor_dist:
                menor_dist = distancias[nombre]
                actual = nombre

        if actual is None:
            break  # no quedan nodos accesibles

        if actual == destino:
            break  # llegamos al destino

        visitados.add(actual)

        # obtener el vértice real desde la tabla hash
        vertice_actual = grafo.vertices.buscar(actual)

        # recorrer sus conexiones
        for arista in vertice_actual.conexiones:
            vecino = arista.destino
            peso = arista.distancia

            nueva_dist = distancias[actual] + peso

            # relajación
            if nueva_dist < distancias[vecino]:
                distancias[vecino] = nueva_dist
                padre[vecino] = actual

    # Reconstruir camino
    camino = []
    nodo = destino

    if distancias[destino] == float("inf"):
        return None, None

    while nodo is not None:
        camino.insert(0, nodo)
        nodo = padre[nodo]

    return camino, distancias[destino]
