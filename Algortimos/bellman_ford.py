
from Eventos.eventos import obtener_distancia

def bellman_ford(grafo, inicio):
    # Validar existencia del nodo inicial
    if grafo.vertices.buscar(inicio) is None:
        print(f"El nodo {inicio} no existe.")
        return None, None

    # === Inicialización ===
    distancias = {}
    padre = {}

    for nombre, vertice in grafo.vertices.items():
        distancias[nombre] = float("inf")
        padre[nombre] = None

    distancias[inicio] = 0

    # === Relajación de aristas (|V|-1 veces) ===
    num_vertices = len(list(grafo.vertices.items()))

    for _ in range(num_vertices - 1):
        for nombre, vertice in grafo.vertices.items():
            for arista in vertice.conexiones:
                u = nombre
                v = arista.destino
                peso = obtener_distancia(arista)

                if distancias[u] != float("inf") and distancias[u] + peso < distancias[v]:
                    distancias[v] = distancias[u] + peso
                    padre[v] = u


    # === Detección de ciclos negativos ===
    for nombre, vertice in grafo.vertices.items():
        for arista in vertice.conexiones:
            u = nombre
            v = arista.destino
            peso = obtener_distancia(arista)

            if distancias[u] != float("inf") and distancias[u] + peso < distancias[v]:
                print("⚠️ El grafo contiene un ciclo negativo.")
                return None, None

    return distancias, padre


