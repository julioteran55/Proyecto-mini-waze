# Eventos externos que afectan el peso original
eventos = {}   # clave: (origen, destino) → factor , aquí pondremos cosas como tráfico, accidetnes o calles cerradas 

#usaremos factores para modificar el peso dependiendo de la situación que ocurra
FACTORES = {
    "normal": 1, 
    "intermedio": 1.5,
    "alto": 2,
    "accidente": 3,
    "cerrada": 9999
}

def agregar_trafico(origen, destino, nivel):
    eventos[(origen, destino)] = FACTORES[nivel]

def agregar_accidente(origen, destino):
    eventos[(origen, destino)] = FACTORES["accidente"]

def cerrar_calle(origen, destino):
    eventos[(origen, destino)] = FACTORES["cerrada"]

def quitar_evento(origen, destino):
    eventos.pop((origen, destino), None)

#de aquí llamará el algoritmo dijkstra los nuevos pesos y ya no los obtendra directamente del grafo ya que por tráfico,
# accidentes o calles cerradas cambiarían los pesos
def obtener_distancia(arista):
    factor = eventos.get((arista.origen, arista.destino), 1)
    return arista.distancia * factor
