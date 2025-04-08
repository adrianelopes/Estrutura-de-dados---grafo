# -*- coding: utf-8 -*-
from graph import Graph
import argparse

def load_from(fileName):
    f = open(fileName, 'r')
    n = int(f.readline())
    
    g = Graph(n)
    
    l = 0
    for line in f:
        line.strip()
        numeros = line.split("\t")
        c = 0
        for i in numeros:
            if(c == n):
                break
            g.M[l][c] = int(i)
            if int(i) != 0:
                g.L[l].append(c)
            c += 1
        l += 1
    
    return g

# Argumento de linha de comando
parser = argparse.ArgumentParser(description="Executa operações em grafos")
parser.add_argument('--file', required=True, help='Nome do arquivo de entrada com o grafo')
args = parser.parse_args()

file_name = args.file

print("="*60)
print(f"Carregando grafo do arquivo: {file_name}")
print("="*60)
g = load_from(file_name)
g.print()

print("\n" + "="*60)
print("Número de Componentes Conexos")
print("="*60)
n = g.num_comp()
print(f"-> Total: {n}")

print("\n" + "="*60)
print("Busca em Largura (BFS) a partir do vértice 0")
print("="*60)
D, pred = g.bfs(0)

print("\n" + "="*60)
print("Caminhos gerados pelo BFS")
print("="*60)
for destino in [2, 3, 5]:
    if destino < g.num_vertices:
        print(f"\nCaminho de 0 até {destino}:")
        g.imprime_caminho_bfs(pred, 0, destino)
    else:
        print(f"\nVértice {destino} não existe no grafo.")

print("\n" + "="*60)
print("Busca em Profundidade Iterativa (DFS)")
print("="*60)
g.dfs_iterativo()
