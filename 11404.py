# 플로이드
from math import inf
import sys
n = int(sys.stdin.readline())
m =int(sys.stdin.readline())
graph = [[inf]*n for _ in range(n)]
for _ in range(m):
    a, b, c = (list(map(int, sys.stdin.readline().split()))) #메모리를 줄이는 방법
    graph[a-1][b-1] = min(graph[a-1][b-1],c)

for k in range(n):
    graph[k][k] = 0
    for i in range(n):
        for j in range(n):
            graph[i][j] =  min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(n):
    for j in range(n):
        if graph[i][j] == inf:
            graph[i][j] = 0
    print(*graph[i])