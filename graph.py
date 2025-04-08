# -*- coding: utf-8 -*-
import queue

class Graph:
    def __init__(self, n):
        self.num_vertices = n
        self.M = [[0 for _ in range(n)] for _ in range(n)]
        self.L = [ [] for _ in range(n)]

    def print(self):
        print("Número de Vértices: " + str(self.num_vertices))
        print("Matriz de adjacência:")
        print(self.M)
        print("Lista de Adjacência:")
        print(self.L)
    
    def num_comp(self):
        pred = self.dfs()
        num = 0
        for v in range(self.num_vertices):
            if(pred[v] == -1):
                num += 1
        return num
    
    def dfs(self):
        pred = [-1 for _ in range(self.num_vertices)]
        visitados = [False for _ in range(self.num_vertices)]
        for v in range(self.num_vertices):
            if(visitados[v] == False):
                self.dfs_rec(v, visitados, pred)
                
        return pred
        
        
    def dfs_rec(self, v, visitados, pred):
        print("Vertice: " + str(v))
        visitados[v] = True
        for u in self.L[v]:
            if(visitados[u] == False):
                pred[u] = v
                self.dfs_rec(u, visitados, pred)
                
                
    def dfs_iterativo(self):
        #Tarefa:  Reimplemente o DFS com auxílio de uma pilha para eliminar a recursão da implementação.
        pred = [-1 for _ in range(self.num_vertices)]
        visitados = [False for _ in range(self.num_vertices)]
        
        for inicio in range(self.num_vertices):
            if not visitados[inicio]:
                pilha = [inicio]  # Cria uma nova pilha com o vértice inicial da componente
                while pilha:
                    v = pilha.pop()
                    if not visitados[v]:
                        print("Visitando (iterativo): " + str(v))
                        visitados[v] = True
                        #  Inverte a ordem dos vizinhos para simular a ordem da recursão
                        for u in reversed(self.L[v]):
                            if not visitados[u]:
                                pilha.append(u)
                                if pred[u] == -1:
                                    pred[u] = v
        return pred
    
    def bfs(self, source):
        visitados = [False for _ in range(self.num_vertices)]
        pred = [-1 for _ in range(self.num_vertices)]
        D = [-1 for _ in range(self.num_vertices)]
        Q = queue.Queue()
        Q.put(source)
        visitados[source] = True
        D[source] = 0
        
        while(Q.empty() == False):
            v = Q.get()
            print("Vertice:" + str(v))
            for u in self.L[v]:
                if(visitados[u] == False):
                    Q.put(u)
                    visitados[u] = True
                    D[u] = D[v] + 1
                    pred[u] = v
        
        return D, pred
    
    def imprime_caminho_bfs(self,pred, s, t):
        #Tarefa: Criar uma função que imprima o caminho entre dois vértices s e t formado pelo BFS. Indicar que “não há caminho entre os vértices” caso não haja o caminho.
        _, pred = self.bfs(s) # Executa BFS a partir de s
        caminho = []
        atual = t
        while atual != -1: 
            caminho.append(atual) # Adiciona o vértice atual ao caminho
            if atual == s:  # Se chegou ao vértice de origem, para o loop
                break
            atual = pred[atual] # Volta o caminho, seguindo os predecessores
        caminho.reverse() 
        if caminho[0] == s:
            print("Caminho de", s, "até", t, ":", caminho)
        else:
            print("Não há caminho entre", s, "e", t)

        