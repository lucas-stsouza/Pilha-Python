from collections import deque

class Fila():
    def __init__(self):
        self.elemento = deque()

    def insere(self, elem):
        self.elemento.append(elem)

    def remove(self):
        return self.elemento.popleft()

    def vazia(self):
        return not bool(self.elemento)

    def tamanho(self):
        return len(self.elemento)

    def inversa(self):
        self.elemento.reverse()