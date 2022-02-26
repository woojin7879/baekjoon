#내리막 길
import sys
m, n = map(int, sys.stdin.readline().split())
graph = []
for _ in range(m):
    graph.append(list(map(int, sys.stdin.readline().split())))
visit = [[-1] * n for _ in range(m)]
visit[-1][-1] = 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y):
    if x == m-1 and y == n-1:
        return 1
    if visit[x][y] != -1:
        return visit[x][y]
    visit[x][y] = 0  
    for i in range(4):
        a = x + dx[i]
        b = y + dy[i]
        if ((0 <= a < m) & (0 <= b < n)):
            if graph[a][b] < graph[x][y]:
                visit[x][y] += dfs(a, b)
    return visit[x][y]
dfs(0,0)
print(visit[0][0])