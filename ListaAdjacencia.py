import ListaEncadeada

class ListaAdjacencia:
    def __init__(self):
        self.Dic = {}

    def AdicionarVertice(self, nome):
        if nome not in self.Dic:
            self.Dic[nome] = ListaEncadeada.ListaEncadeada()
            return True
        return False

    def InserirAresta(self, ver1, ver2, peso):
        pesoint = int(peso)
        self.AdicionarVertice(ver1)
        self.AdicionarVertice(ver2)
        self.Dic[ver1].Adiciona(ver2, pesoint)
        self.Dic[ver2].Adiciona(ver1, pesoint)
        return True

    def ImprimirGrafo(self):
        
        for vertice in sorted(self.Dic.keys()):
            print(f"{vertice}: ", end="")
            self.Dic[vertice].ImprimiLista()

    def ObterVertices(self):
        return list(self.Dic.keys())