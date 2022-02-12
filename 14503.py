#로봇청소기
from collections import deque
import sys
n, m = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
array = []
visit = [[0]*m for _ in range(n)]
for _ in range(0,n):
    array.append(list(map(int, input().split())))

di = [-1,0,1,0]
dj = [0,1,0,-1]

deq = deque()

deq.append([r,c,d])
num = 0

while deq:
    flag = False
    i, j, direction = deq.popleft()
    if visit[i][j] == 0:
        visit[i][j] = 1
        num += 1
    for k in range(3,-1,-1):
        a = i + di[(direction + k)%4]
        b = j + dj[(direction + k)%4]
        if (0 <= a < n) & (0 <= b < m):
            if (array[a][b] == 0) & (visit[a][b] == 0):
                deq.append([a,b,(direction+k)%4])
                break
        if k == 0:
            flag = True
    if flag:
        a = i - di[direction]
        b = j - dj[direction]
        if (0 <= a < n) & (0 <= b < m):
            if array[a][b] == 0:
                deq.append([a,b,direction])
            else:
                break
        else:
            break
print(num)
