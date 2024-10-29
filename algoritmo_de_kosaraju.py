from collections import defaultdict

# Classe para o grafo
class Grafo:
    def __init__(self, vertices):
        self.V = vertices                         # Número de vértices
        self.grafo = defaultdict(list)            # Grafo original
        self.grafo_reverso = defaultdict(list)    # Grafo com arestas revertidas

    # Adiciona uma aresta ao grafo
    def adicionar_aresta(self, u, v):
        self.grafo[u].append(v)

    # Realiza a DFS e registra a ordem de término dos nós
    def dfs_ordem(self, v, visitado, ordem):
        visitado[v] = True
        for vizinho in self.grafo[v]:
            if not visitado[vizinho]:
                self.dfs_ordem(vizinho, visitado, ordem)
        ordem.append(v)

    # Realiza a DFS no grafo revertido e encontra os componentes
    def dfs_componente(self, v, visitado, componente):
        visitado[v] = True
        componente.append(v)
        for vizinho in self.grafo_reverso[v]:
            if not visitado[vizinho]:
                self.dfs_componente(vizinho, visitado, componente)

    # Cria o grafo reverso (inverso das arestas)
    def inverter_grafo(self):
        for u in self.grafo:
            for v in self.grafo[u]:
                self.grafo_reverso[v].append(u)

    # Executa o algoritmo de Kosaraju
    def kosaraju(self):
        # Passo 1: Realiza a primeira DFS para calcular a ordem de término
        visitado = [False] * self.V
        ordem = []
        
        for i in range(self.V):
            if not visitado[i]:
                self.dfs_ordem(i, visitado, ordem)
        
        # Passo 2: Inverte o grafo
        self.inverter_grafo()
        
        # Passo 3: Realiza DFS no grafo invertido na ordem reversa dos nós de término
        visitado = [False] * self.V
        componentes_fortemente_conexos = []
        
        while ordem:
            v = ordem.pop()
            if not visitado[v]:
                componente = []
                self.dfs_componente(v, visitado, componente)
                componentes_fortemente_conexos.append(componente)
        
        return componentes_fortemente_conexos

# Exemplo de uso
if __name__ == "__main__":
    g = Grafo(5)
    g.adicionar_aresta(1, 0)
    g.adicionar_aresta(0, 2)
    g.adicionar_aresta(2, 1)
    g.adicionar_aresta(0, 3)
    g.adicionar_aresta(3, 4)
    
    cfc = g.kosaraju()
    print("Componentes Fortemente Conexos:")
    for componente in cfc:
        print(componente)
