#벽 부수고 이동하기
from collections import deque
import sys
n, m = map(int, sys.stdin.readline().split())
array = []
visit = [[[0] * m for _ in range(n)] for _ in range(2)]
num = n*m +1
for _ in range(n):
    array.append(list(map(int, sys.stdin.readline().rstrip())))
dx = [0,0,1,-1]
dy = [1,-1,0,0]

deq =  deque()
deq.append([0,0,0])
visit[0][0][0] = 1
while deq:
    x, y, wall = deq.popleft()
    if x==n-1 and y==m-1:
        num = min(num, visit[wall][x][y])
    for i in range(4):
        a = x + dx[i] 
        b = y + dy[i]
        if ((0 <= a < n) & (0 <= b < m)):
            if array[a][b] == 0 and visit[wall][a][b]== 0:
                visit[wall][a][b] = visit[wall][x][y] + 1
                deq.append([a,b,wall])
            elif array[a][b] == 1 and wall == 0:
                visit[1][a][b] = visit[wall][x][y] + 1
                deq.append([a,b,1])
if num == n*m +1:
    print(-1)
else:
    print(num)