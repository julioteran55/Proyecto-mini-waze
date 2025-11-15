
#Código de hash table visto en clase pero pasado a python.


class Entrada:
    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor
        self.eliminado = False


class TablaHash:
    DEFAULT_SIZE = 6

    def __init__(self, tamaño=DEFAULT_SIZE):
        self.tamaño = tamaño
        self.num_claves = 0
        self.bins = [None] * tamaño  # lista de slots

    # Función hash usando método de multiplicación 
    def funcion_hash(self, clave):
        hash_val = 0
        for c in clave:
            hash_val = (hash_val * 31 + ord(c)) % self.tamaño
        return hash_val

    # INSERTAR con linear probing
    def insertar(self, clave, valor):
        if self.num_claves == self.tamaño:
            return False  # tabla llena

        indice = self.funcion_hash(clave)
        contador = 0

        while self.bins[indice] is not None and contador < self.tamaño:
            # Si la clave ya existe → actualizar
            if not self.bins[indice].eliminado and self.bins[indice].clave == clave:
                self.bins[indice].valor = valor
                return True

            indice = (indice + 1) % self.tamaño
            contador += 1

        # Insertar nueva entrada
        self.bins[indice] = Entrada(clave, valor)
        self.num_claves += 1
        return True

    # BUSCAR con linear probing
    def buscar(self, clave):
        indice = self.funcion_hash(clave)
        contador = 0

        while self.bins[indice] is not None and contador < self.tamaño:
            if not self.bins[indice].eliminado and self.bins[indice].clave == clave:
                return self.bins[indice].valor

            indice = (indice + 1) % self.tamaño
            contador += 1

        return None  # no encontrado

    # ELIMINAR marcando como deleted
    def eliminar(self, clave):
        indice = self.funcion_hash(clave)
        contador = 0

        while self.bins[indice] is not None and contador < self.tamaño:
            if not self.bins[indice].eliminado and self.bins[indice].clave == clave:
                self.bins[indice].eliminado = True
                self.num_claves -= 1
                return True

            indice = (indice + 1) % self.tamaño
            contador += 1

        return False  # no se encontró

    # Mostrar la tabla hash
    def mostrar(self):
        for i in range(self.tamaño):
            slot = self.bins[i]
            print(f"[{i}]: ", end="")
            if slot is None:
                print("null")
            elif slot.eliminado:
                print("eliminado")
            else:
                print(f"({slot.clave}, {slot.valor})")

    #código sacado de stackoverflow, este método replica el funcionamiento del metodo .items() de un diccionario de python
    #que utilizaremos más adelante
    def items(self):
        for slot in self.bins:
            if slot is not None and not slot.eliminado:
                yield slot.clave, slot.valor
