import matplotlib.pyplot as plt
import networkx as nx

def dibujar_grafo(grafo):
    G = nx.DiGraph()  # grafo dirigido (con flechas)

    # Usamos tu estructura: grafo.vertices
    for origen, vertice in grafo.vertices.items():
        for arista in vertice.conexiones:
            G.add_edge(origen, arista.destino, weight=arista.distancia)

    # Posición de nodos automática
    pos = nx.spring_layout(G, seed=42)

    # Dibujar nodos y conexiones
    nx.draw(G, pos,
            with_labels=True,
            node_color="skyblue",
            node_size=1500,
            font_weight="bold",
            arrows=True,
            connectionstyle="arc3,rad=0.1")

    # Mostrar las distancias como etiquetas
    etiquetas = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=etiquetas)

    plt.title("Mapa de calles (grafo con direcciones y pesos)")
    plt.show()

