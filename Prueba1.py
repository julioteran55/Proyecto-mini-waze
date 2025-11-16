from Estructuras.Grafo import Grafo 
from Algortimos.dijkstra import dijkstra
from Algortimos.BFS import bfs
from Algortimos.utils import reconstruir_camino
from Algortimos.bellman_ford import bellman_ford
from cargarDatos import cargar_grafo_desde_csv

ciudad = cargar_grafo_desde_csv("calles.csv")

#Dijkstra
camino, distancia = dijkstra(ciudad, "H1", "UL")
print("-------------Dijkstra------------------")
print("Camino:", camino)
print("Distancia:", distancia)

print()
#BFS, buscando el camino con menos saltos 
camino_bfs = bfs(ciudad, "H1", "UL")
print("-------------BFS------------------")
print("Camino BFS:", camino_bfs)

print()
#bellman_ford
distancias_bf, padre_bf = bellman_ford(ciudad, "H1")
camino_bf = reconstruir_camino(padre_bf, "UL")
print("-------------Bellman Ford------------------")
print("Bellman-Ford → Camino:", camino_bf)
print("Bellman-Ford → Distancia:", distancias_bf["UL"])
