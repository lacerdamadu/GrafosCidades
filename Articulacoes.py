class PontosArticulacoes:
    def __init__(self, grafo):
        #Pega o grafo
        self.grafo = grafo

        #Qual o tempo/"passada" em que cada vértice foi descoberto na dfs
        self.tempo = 0

        #Guarda quais vértices já foram explorados na árvore
        self.visitado = {}

        #Guarda qual o vértice mais "antigo" que cada um consegue acessar
        self.baixo = {}

        #Guarda qual é o vértice que descobriu cada na árvore de profundidade
        self.pai = {}

        #Guarda as articulações
        self.articulacoes = set()
    
    def EncontraArticulacoes(self):
        # Inicializa estruturas
        for vertice in self.grafo.Dic.keys():
            #Coloca que nenhum dos vértices foi visitado
            self.visitado[vertice] = False

            #Inicia o baixo de cada vértice como infinito -> como se afirmasse que não existe ainda forma conhecido de se chegar num vértice mais antigo
            self.baixo[vertice] = float('inf')

            #Inicia os pais de todos os vértices como ninguém
            self.pai[vertice] = None
        
        #Realiza a busca em profundidade para os vértices que não foram visitados
        inicio = 0
        for vertice in self.grafo.Dic.keys():
            if not self.visitado[vertice]:
                print(f"Iniciando o subgrafo conexo em {vertice}")
                self._dfs(vertice)
                if inicio != 0:
                    print("Grafo desconexo")
                inicio += 1
        
        return self.articulacoes

    #Buca em profundidade adaptada para achar os pontos de articulação
    def _dfs(self, u): 
        # Marca como visitado e inicializa valores
        self.visitado[u] = True

        #Inicialmente coloca que baixo de um vértice é o próprio tempo em que foi descoberto
        self.baixo[u] = self.tempo

        #Salva o tempo atual em uma variável auxiliar
        disc = self.tempo

        #Atualiza o tempo
        self.tempo += 1
        
        filhos = 0
        
        # Percorre todos os vizinhos
        current = self.grafo.Dic[u].cabeca

        '''Enquanto o vértice que está sendo visitado não for "None" o código itera. 
        Quando parar signifca que aquela componente conexa já teve todos os seus vértices explorados'''

        while current:
            #Pega o nome do primeiro vizinho de u
            v = current.dado
            
            if not self.visitado[v]:
                # Se v não foi visitado, é filho de u na árvore DFS
                self.pai[v] = u

                filhos += 1

                # v passa a ser u e o processo é repetido até um dos filhos não ter mais vizinhos não explorados
                self._dfs(v)
                
                # Verifica se a subárvore de v tem conexão com ancestrais de u
                # Procurando arestas de retorno
                self.baixo[u] = min(self.baixo[u], self.baixo[v])
                
                # u é ponto de articulação se:
                # É raiz e tem pelo menos 2 filhos
                if self.pai[u] is None and filhos > 1:
                    self.articulacoes.add(u)
                
                '''Não é raiz e tem um filho tal que a subárvore na qual esse filho é raiz não tem nenhum outro vértice que tem arestas de retorno para um ancestral de u'''
                # Isso é descoberto usando baixo[v] >= descoberta[u]
                if self.pai[u] is not None and self.baixo[v] >= disc:
                    self.articulacoes.add(u)

            # Se o vértice já tiver sido visitado E não for o pai de u, estamos numa aresta de retorno    
            # Isso significa que encontramos um caminho alternativo para um vértice já visitado
            elif v != self.pai[u]:  
                self.baixo[u] = min(self.baixo[u], self.baixo[v])
            
            current = current.proximo

#Para chamar essa classe no código, usar essas instruções:

# from Articulacoes import PontosArticulacoes
    
# finder = PontosArticulacoes(grafo)
# pontos_articulacao = finder.EncontraArticulacoes()

# if pontos_articulacao:
#     print(f"Pontos de articulação encontrados: {sorted(pontos_articulacao)}")
# else:
#     print("Não há pontos de articulação neste grafo")
