import ListaAdjacencia
import Impressao

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



def main():
    print("Bem-vindo ao sistema de criação e manipulação de grafos!")
    NomeArquivo = input("Digite o nome do arquivo formatado: ")
    try:
        linhas = LeituraArquivo(NomeArquivo)
        grafo = ListaAdjacencia.ListaAdjacencia()
        
        for linha in linhas:
            if len(linha) >= 3:  # Verifica se tem vértice1, vértice2, peso
                grafo.InserirAresta(linha[0], linha[1], linha[2])

        print("Grafo Inicializado com sucesso!")
        print("Deseja realizar qual operação?")
        escolha = 1
        while(escolha != "0"):
            print("(0)Finalizar programa\n" \
            "(1)Retornar o numero de cidades no grafo\n" \
            "(2)Retornar a quantidade de estradas no grafo\n" \
            "(3)Retornar os vizinhos de uma cidade fornecida\n" \
            "(4)Determinar a quantidade de vizinhos de uma cidade fornecida\n"\
            "(5)Calcular o menor caminho entre duas cidades escolhidas\n"\
            "(6)Verificar se a rede e conexa\n" \
            "(7)Identificar se a empresa consegue criar uma passeio turistico\n" \
            "(8)Imprimir Lista de Adjacencia\n" \
            "(9)Imprimi grafo em uma imagem\n")
            escolha = input()
        
            if(escolha == "0"):
                break
            elif(escolha == "1"):
                print(f"O numero de cidades no grafo é {grafo.ObterNumCidades()}")

            elif(escolha == "2"):
                print(f"O numero de estradas no grafo é {grafo.ObterNumEstradas()}")

            elif(escolha == "3"):
                cidade = input("Digite uma cidade para ver os vizinhos:")
                print(f"Os vizinhos da cidade {cidade} são : {grafo.RetornarVizinhos(cidade)}")

            elif(escolha == "4"):
                cidade = input("Digite uma cidade para ver a quantidade de vizinhos: ")
                print(f"Quantidade de vizinhos de {cidade}: {grafo.QuantidadeVizinhos(cidade)}")

            elif(escolha == "5"):
                origem = input("Digite a cidade de origem: ")
                destino = input("Digite a cidade de destino: ")
                dist, caminho = grafo.MenorCaminho(origem, destino)
                if dist is None:
                    print("Nao existe caminho entre as cidades.")
                else:
                    print(f"Menor distancia {origem} -> {destino} = {dist}")
                    print("Caminho:", " -> ".join(caminho))

            elif(escolha == "6"):
                if(grafo.RedeConexa()):
                    print("A rede e conexa!")
                else:
                    print("A rede nao e conexa")
        
            elif(escolha == "7"):
                if(grafo.Ciclos()):
                    print(f"O grafo possui ciclo.Exemplo: {grafo.Ciclos()}")
                else:
                    print("Grafo nao possui ciclo.")

            elif(escolha == "8"):
                grafo.ImprimirGrafo()
            elif(escolha == "9"):
                Impressao.Imprimir(NomeArquivo)
            elif(escolha > 9 or escolha < 0):
                print("Numero digitado fora do intervalo!")
    except FileNotFoundError:
        print(f"Erro: Arquivo '{NomeArquivo}' não encontrado!")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()