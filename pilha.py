class Pilha:
    def __init__(self):
        self.dados = list()

    def __len__(self):
        return len(self.dados)

    def empilhe(self, item):
        self.dados.append(item)

    def desempilhe(self):
        return self.dados.pop()

    def topo(self):
        return self.dados[-1]

    def vazio(self):
        return self.dados == []