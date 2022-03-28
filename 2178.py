#미로 탐색
import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
visit = [[False] * m for _ in range(n)]
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().strip())))
visit[0][0] = True
deq = deque()
deq.append([0,0,1])
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
minimum = n * m + 1
while deq:
    x, y, l = deq.popleft()
    if x == n-1 and y == m-1:
        minimum = min(minimum, l)
        break
    for i in range(4):
        a = x + dx[i]
        b = y + dy[i]
        if 0 <= a < n and 0 <= b < m:
            if visit[a][b] == False and graph[a][b] == 1:
                visit[a][b] = True
                deq.append([a, b, l + 1])
    visit[x][y] = False
print(minimum)