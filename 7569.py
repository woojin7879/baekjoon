#토마토
from collections import deque
import sys
m, n, h = map(int, sys.stdin.readline().split())
array = [[] for _ in range(h)]
num = 1
zero = False
for i in range(h):
    for j in range(n):
        array[i].append(list(map(int, input().split())))
deq = deque() 
for i in range(h):
    for j in range(n):
        for k in range(m):
            if array[i][j][k] == 1:
                deq.append([i,j,k])
dx = [0,0,1,-1,0,0]
dy = [0,0,0,0,1,-1]
dz = [1,-1,0,0,0,0]
while deq:
    z, y, x = deq.popleft()
    for i in range(6):
        a = z + dz[i]
        b = y + dy[i]
        c = x + dx[i]
        if ((0 <= a < h) & (0 <= b < n) & (0 <= c < m)):
            if array[a][b][c] == 0:
                array[a][b][c] = array[z][y][x] + 1
                deq.append([a,b,c])
                num = max(num, array[a][b][c])

for i in array:
    for j in i:
        if 0 in j:
            zero = True

if zero:
    print(-1)
else:
    print(num-1)