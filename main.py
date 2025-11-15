# archivo: main.py
from Estructuras.Grafo import Grafo 
from Algortimos.dijkstra import dijkstra
from Algortimos.BFS import bfs
#from graficarMapa import dibujar_grafo
ciudad = Grafo()

# Crear calles (origen, destino, distancia, bidireccional) esa es la estru tura de los agumentos
ciudad.agregar_calle("A", "B", 4, True)
ciudad.agregar_calle("A", "C", 2, False)
ciudad.agregar_calle("B", "D", 5, True)
ciudad.agregar_calle("C", "D", 8, False)
ciudad.agregar_calle("D", "E", 3, True)
ciudad.agregar_calle("E", "F", 6, False)
ciudad.mostrar_mapa()

camino, distancia = dijkstra(ciudad, "A", "D")

print("Camino:", camino)
print("Distancia:", distancia)
#dibujar_grafo(ciudad)


#BFS, buscando el camino con menos saltos 
camino_bfs = bfs(ciudad, "A", "E")
print("Camino BFS:", camino_bfs)