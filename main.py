import ListaAdjacencia
import Articulacoes

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
        
        grafo.ImprimirGrafo()
        
    except FileNotFoundError:
        print(f"Erro: Arquivo '{NomeArquivo}' não encontrado!")
    except Exception as e:
        print(f"Erro inesperado: {e}")


if __name__ == "__main__":
    main()