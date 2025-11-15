"""
Simulación del mapa 
-----------------------------------
Objetivo: Construir manualmente un grafo dirigido
para representar las calles de una ciudad pequeña.
"""

from .HashTable import TablaHash

class Arista:
    def __init__(self, origen, destino, distancia, bidireccional=False):
        self.origen = origen
        self.destino = destino
        self.distancia = distancia
        self.bidireccional = bidireccional

class Vertice:
    def __init__(self, nombre):
        self.nombre = nombre
        self.conexiones = []  # lista de Aristas

    def agregar_conexion(self, destino, distancia, bidireccional=False):
        arista = Arista(self.nombre, destino, distancia, bidireccional)
        self.conexiones.append(arista)

class Grafo:
    def __init__(self):
        self.vertices = TablaHash() # nombre → Vertice
        #se uso hashTables

    def agregar_vertice(self, nombre):
        if self.vertices.buscar(nombre) is None:
            self.vertices.insertar(nombre, Vertice(nombre))

    def agregar_calle(self, origen, destino, distancia, bidireccional=False):
        # Creamos los vértices si no existen
        if origen == destino:
            print(f"Mismo destino y origen no se agrega la calle")
            return
        self.agregar_vertice(origen)
        self.agregar_vertice(destino)

        # Agregamos conexión
        self.vertices.buscar(origen).agregar_conexion(destino, distancia, bidireccional)

        # Si es bidireccional, agregamos la vuelta
        if bidireccional:
            self.vertices.buscar(destino).agregar_conexion(origen, distancia, bidireccional)

    def mostrar_mapa(self):
        print("\n Mapa de la ciudad (grafo de calles):\n")
        for nombre, vertice in self.vertices.items():
            print(f" {nombre} :  ", end="")
            if len(vertice.conexiones) == 0:
                print("sin conexiones")
                continue
            conexiones = []
            for arista in vertice.conexiones:
                sentido = "<->" if arista.bidireccional else "→"
                conexiones.append(f"{sentido} {arista.destino} ({arista.distancia} km)")
            print(", ".join(conexiones))

 