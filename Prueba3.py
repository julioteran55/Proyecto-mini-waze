from Estructuras.Grafo import Grafo 
from Algortimos.dijkstra import dijkstra
from Eventos.eventos import agregar_accidente , agregar_trafico , cerrar_calle , quitar_evento , eventos 
from cargarDatos import cargar_grafo_desde_csv

ciudad = cargar_grafo_desde_csv("calles.csv")

camino, distancia = dijkstra(ciudad, "J1", "J")
print("Camino:", camino)
print("Distancia:", distancia)

#agregamos tráfico
agregar_trafico("T","V","alto")
#agregamos accidente
agregar_accidente("V","W")

print()
print("Después de eventos:")
#volvemos a imprimir
camino, distancia = dijkstra(ciudad, "J1", "J")
print()

print("Camino:", camino)
print("Distancia:", distancia)