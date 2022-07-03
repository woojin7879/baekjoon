import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
visit = [[False] * m for _ in range(n)]
graph = []
for _ in range(n):
    graph.append(list(map(str, sys.stdin.readline().strip())))
dnum = 0
bnum = 0
deq = deque() 
for i in range(0,n):
    for j in range(0,m):
        if graph[i][j] == 'o':
            deq.append([i,j])
            dnum += 1
        if graph[i][j] == 'v':
            bnum += 1
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
maxb = 0
maxd = 1
while deq:
    x, y= deq.popleft()
    if visit[x][y] == True and graph[x][y] == 'o':
        continue
    else:
        if (maxb + maxd) > 1 and graph[x][y] == 'o':
            if maxb < maxd:
                bnum -= maxb
            else:
                dnum -= maxd
            maxb = 0
            maxd = 1
        visit[x][y] = True
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if 0 <= a < n and 0 <= b < m:
                if visit[a][b] == False:
                    if graph[a][b] == '.':
                        visit[a][b] = True
                        deq.appendleft([a, b])
                    elif graph[a][b] == 'v':
                        visit[a][b] = True
                        deq.appendleft([a, b])
                        maxb += 1
                    elif graph[a][b] == 'o':
                        visit[a][b] = True
                        deq.appendleft([a, b])
                        maxd += 1
if (maxb + maxd) > 1:
    if maxb < maxd:
        bnum -= maxb
    else:
        dnum -= maxd
print(dnum, bnum)