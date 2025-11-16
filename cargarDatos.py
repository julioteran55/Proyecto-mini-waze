import csv
from Estructuras.Grafo import Grafo 

def cargar_grafo_desde_csv(nombre_archivo):
    grafo = Grafo()
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            origen = str(fila["origen"].strip())
            distancia = float(fila["distancia"].strip())
            destino = str(fila["destino"].strip())
            bidireccional = fila["bidireccional"].strip().lower() == "true"
            grafo.agregar_calle(origen, destino, distancia, bidireccional)
    return grafo
