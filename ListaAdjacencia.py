import ListaEncadeada

NUMCAMINHOS = 1

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
    
    def CalculaCiclos(self,v, pai, caminho, inicio,ciclos):
        caminho.append(v)   #quarda um verticie em um caminho atual 

        atual = self.Dic[v].cabeca
        while atual:
            vizinho = atual.dado
            if vizinho not in caminho:
                self.CalculaCiclos(vizinho, v, caminho, inicio,ciclos)
            elif vizinho != pai and vizinho == inicio and len(caminho) >= 4: 
                # se a proxima aresta nao é o pai, nao ter uma caminho de volta
                # Para ver ser o proximo verticie é o primeiro verticie do caminho confirma o ciclo
                # Se o caminho tem mais de 4 arestas 
                ciclo = caminho + [vizinho]
                if len(ciclos) >= NUMCAMINHOS:
                    return ciclos    
                if ciclo not in ciclos:
                    ciclos.append(ciclo)
            atual = atual.proximo
        caminho.pop()
    
    def Ciclos(self): #retorna um vetor que tem tamanho NUMCAMINHOS com vetores dos caminhos percorridos
        ciclos = []
        for vertice in self.Dic:
            caminho = []
            if len(ciclos) >= NUMCAMINHOS:
                return ciclos
            self.CalculaCiclos(vertice, None, caminho, vertice,ciclos)
        return ciclos