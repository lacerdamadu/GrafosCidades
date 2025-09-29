class No:
    def __init__(self, dado, peso) -> None:
        self.dado = dado
        self.proximo = None
        self.peso = peso

class ListaEncadeada:

    def __init__(self) -> None:
        #Cria uma lista encadeada vazia
        self.cabeca = None
    
    def Adiciona(self, dado, peso) -> None:
        #Esta funcao sempre ira adicionar os elementos no final da lista
        novo = No(dado, peso)
        if self.cabeca == None: #Verifica se a lista esta vazia
            novo.proximo = self.cabeca #Como ela vai estar vazia o proximo é None
            self.cabeca = novo
        else:
            noatual = self.cabeca
            while noatual.proximo != None: #Encontra o último elemento da lista
                noatual = noatual.proximo
            
            noatual.proximo = novo
            novo.proximo = None
    def ImprimiLista(self):
        #Percorre a lista encadeada para realizar a impressão
        current = self.cabeca
        while current:
            print(f"-> [{current.dado}-{current.peso}]", end=" ")
            current = current.proximo
        print()
    
