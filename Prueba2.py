from Estructuras.Grafo import Grafo 
from Algortimos.dijkstra import dijkstra
from Eventos.eventos import agregar_accidente , agregar_trafico , cerrar_calle , quitar_evento , eventos 
ciudad = Grafo()

# Crear calles (origen, destino, distancia, bidireccional) esa es la estru tura de los agumentos
ciudad.agregar_calle("A", "B", 4, True)
ciudad.agregar_calle("A", "C", 2, False)
ciudad.agregar_calle("B", "D", 5, True)
ciudad.agregar_calle("C", "D", 8, False)
ciudad.agregar_calle("D", "E", 3, True)
ciudad.agregar_calle("E", "F", 6, False)
ciudad.mostrar_mapa()

camino, distancia = dijkstra(ciudad, "A", "E")
print("Camino:", camino)
print("Distancia:", distancia)

#cerramos calle
cerrar_calle("A","B")

#volvemos a imprimir
camino, distancia = dijkstra(ciudad, "A", "E")


print("Camino:", camino)
print("Distancia:", distancia)



