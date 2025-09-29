import networkx as nx
import matplotlib.pyplot as plt

def LeituraArquivo(NomeArquivo):
    arq = open(NomeArquivo)
    linhas = arq.readlines()
    x = 0
    while x < len(linhas):
        if linhas[x] == "\n":
            local = linhas.index(linhas[x])
            linhas.pop(local)
        else:
            linhas[x] = linhas[x].split(',')
            x += 1

    for i in linhas:
        local = linhas.index(i) 
        for b in i:
            local2 = linhas[local].index(b) 
            if "\n" in b:
                linhas[local][local2] = b.replace("\n",'')
    return linhas

class Grafo:

    def __init__(self):
        self.grafo = nx.Graph() #Cria um objeto da classe Graph logo toda vez que utilizarmos a um objeto da classe Grafo é necessário utilizar .grafo
    
    def Insere(self, linhas):
        for i in range(len(linhas)):
            ver1 =  linhas[i][0]
            ver2 = linhas[i][1]
            peso = float(linhas[i][2])
            self.grafo.add_node(ver1)
            self.grafo.add_node(ver2)
            self.grafo.add_edge(ver1, ver2, weight = peso)

    def Impressao(self):
        plt.figure(2)
        pos=nx.spring_layout(G.grafo)
        nx.draw_networkx(G.grafo, pos, with_labels= True, node_color='pink',edge_color='black')

        edge_labels = nx.get_edge_attributes(G.grafo, 'weight')
        nx.draw_networkx_edge_labels(G.grafo, pos, edge_labels=edge_labels, font_size=10, font_weight='bold')

        plt.show()
    

print("Bem-vindo a bibliotecas para manipulação de grafos!")
NomeArquivo = input("Digite o nome do arquivo(incluindo o formato) a ser lido: ")

linhas = LeituraArquivo(NomeArquivo)
G = Grafo()
G.Insere(linhas)
G.Impressao()