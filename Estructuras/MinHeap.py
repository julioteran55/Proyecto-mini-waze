class MinHeap:
    def __init__(self):
        self.heap = []  # lista para almacenar elementos (costo, nodo)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _subir(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index][0] < self.heap[parent][0]:
                self._swap(index, parent)
                index = parent
            else:
                break

    def _bajar(self, index):
        size = len(self.heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < size and self.heap[left][0] < self.heap[smallest][0]:
                smallest = left
            if right < size and self.heap[right][0] < self.heap[smallest][0]:
                smallest = right

            if smallest != index:
                self._swap(index, smallest)
                index = smallest
            else:
                break

    def insertar(self, elemento):
        self.heap.append(elemento)
        self._subir(len(self.heap) - 1)

    def extraer_min(self):
        if not self.heap:
            return None

        minimo = self.heap[0]
        ultimo = self.heap.pop()

        if self.heap:
            self.heap[0] = ultimo
            self._bajar(0)

        return minimo

    def esta_vacio(self):
        return len(self.heap) == 0
