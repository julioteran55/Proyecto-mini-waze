import csv
from Estructuras.Grafo import Grafo 

def cargar_grafo_desde_csv(nombre_archivo):
    grafo = Grafo()
    with open(nombre_archivo, "r") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            origen = fila["origen"]
            destino = fila["destino"]
            distancia = float(fila["distancia"])
            bidireccional = fila["bidireccional"].lower() == "true"
            grafo.agregar_calle(origen, destino, distancia, bidireccional)
    return grafo

# Ej
ciudad = cargar_grafo_desde_csv("calles.csv")
ciudad.mostrar_mapa()
