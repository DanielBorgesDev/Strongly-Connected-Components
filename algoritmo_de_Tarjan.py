from collections import defaultdict

# Classe para o Grafo
class Grafo:
    def __init__(self, vertices):
        self.V = vertices                          # Número de vértices
        self.grafo = defaultdict(list)             # Lista de adjacências
        self.tempo = 0                             # Tempo para marcação de descoberta
        self.resultado = []                        # Lista para armazenar os CFCs

    # Adiciona uma aresta ao grafo
    def adicionar_aresta(self, u, v):
        self.grafo[u].append(v)

    # Função auxiliar de DFS para encontrar CFCs usando Tarjan
    def tarjan_dfs(self, u, descoberto, menor_indice, pilha, esta_na_pilha):
        # Inicializa o índice de descoberta e o menor índice alcançável
        descoberto[u] = menor_indice[u] = self.tempo
        self.tempo += 1
        pilha.append(u)
        esta_na_pilha[u] = True

        # Explora os vizinhos de u
        for vizinho in self.grafo[u]:
            if descoberto[vizinho] == -1:  # Se o vizinho não foi visitado
                self.tarjan_dfs(vizinho, descoberto, menor_indice, pilha, esta_na_pilha)
                menor_indice[u] = min(menor_indice[u], menor_indice[vizinho])
            elif esta_na_pilha[vizinho]:  # Se o vizinho está na pilha
                menor_indice[u] = min(menor_indice[u], descoberto[vizinho])

        # Se u é o início de um componente fortemente conexo
        if menor_indice[u] == descoberto[u]:
            componente = []
            while True:
                v = pilha.pop()
                esta_na_pilha[v] = False
                componente.append(v)
                if v == u:
                    break
            self.resultado.append(componente)

    # Executa o algoritmo de Tarjan para encontrar CFCs
    def tarjan(self):
        descoberto = [-1] * self.V      # Índices de descoberta dos nós
        menor_indice = [-1] * self.V    # Menores índices alcançáveis
        esta_na_pilha = [False] * self.V # Marca os nós que estão na pilha
        pilha = []

        # Executa DFS para cada vértice não visitado
        for i in range(self.V):
            if descoberto[i] == -1:
                self.tarjan_dfs(i, descoberto, menor_indice, pilha, esta_na_pilha)

        return self.resultado

# Exemplo de uso
if __name__ == "__main__":
    g = Grafo(5)
    g.adicionar_aresta(1, 0)
    g.adicionar_aresta(0, 2)
    g.adicionar_aresta(2, 1)
    g.adicionar_aresta(0, 3)
    g.adicionar_aresta(3, 4)
    
    cfc = g.tarjan()
    print("Componentes Fortemente Conexos:")
    for componente in cfc:
        print(componente)
