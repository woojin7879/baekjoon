#아기상어
from collections import deque
from math import inf
import sys
import heapq
n = int(sys.stdin.readline())
graph = []
shark = 2
eat = 0
seccnt = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
sx, sy = 0, 0
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            graph[i][j] = 0
            sx, sy = i, j
            break
while True:
    deq = deque()
    fish = []
    deq.append([sx, sy, 0])
    visit = [[0] * n for _ in range(n)]
    stop = inf
    while deq:
        x, y, move = deq.popleft()
        if move >= stop:
            break
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if ((0 <= a < n) & (0 <= b < n)) and visit[a][b] == 0 and graph[a][b]<=shark:
                if 0 < graph[a][b] < shark:
                    heapq.heappush(fish, [move + 1, a, b])
                    stop = min(stop, move + 1)
                visit[a][b] = 1
                deq.append([a, b, move + 1])
    if len(fish) != 0:
        second, sx, sy = heapq.heappop(fish)
        seccnt += second
        eat += 1
        graph[sx][sy] = 0
        if shark == eat:
            shark += 1
            eat = 0
    else:
        break
print(seccnt)