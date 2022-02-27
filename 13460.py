#구슬 탈출 2
from collections import deque
import sys
n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(str, sys.stdin.readline().strip())))
ball = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'R':
            graph[i][j] = '.'
            rx, ry = i, j
        elif graph[i][j] == 'B':
            graph[i][j] = '.'
            bx, by = i, j
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ball.append([rx, ry, bx, by, 0])
minmove = 11
visit = []
while ball:
    rx, ry, bx, by, move = ball.popleft()
    visit.append([rx, ry, bx, by])
    if move > 10:
        break
    for i in range(4):
        ra, rb, ba, bb = rx, ry, bx, by
        rcnt, bcnt = 0, 0
        while graph[ra + dx[i]][rb + dy[i]] != '#' and graph[ra][rb] != 'O':
            rcnt += 1
            ra += dx[i]
            rb += dy[i]
        while graph[ba + dx[i]][bb + dy[i]] != '#' and graph[ba][bb] != 'O':
            bcnt += 1
            ba += dx[i]
            bb += dy[i]
        if graph[ba][bb] == 'O':
            continue
        if graph[ra][rb] == 'O':
            minmove = min(minmove, move + 1)
        if ra == ba and rb == bb:
            if rcnt > bcnt:
                ra -= dx[i]
                rb -= dy[i]
            else:
                ba -= dx[i]
                bb -= dy[i]
        if [ra, rb, ba, bb] not in visit:
            ball.append([ra, rb, ba, bb, move + 1])
if minmove > 10:
    print(-1)
else:
    print(minmove)