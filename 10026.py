#적록색약
import sys
from collections import deque
n = int(sys.stdin.readline())
array=[]
visit=[[False] * n for _ in range(n)]
realcnt = 0
rgcnt = 0
for _ in range(n):
    array.append(list(map(str, sys.stdin.readline().rstrip())))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

deq = deque() 
def dfs(x,y):
    deq.append([x,y])
    while deq:
        x,y = deq.popleft()
        color = array[x][y]
        for i in range(4):
            a = x + dx[i] 
            b = y + dy[i]
            if ((0 <= a < n) & (0 <= b < n)):
                if ((visit[a][b] == False) & (array[a][b] == color)):
                    visit[a][b] = True
                    deq.append([a,b])

for i in range(n):
    for j in range(n):
        if visit[i][j] == False:
            visit[i][j] = True
            dfs(i,j)
            realcnt +=1

visit=[[False]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if array[i][j] == 'G':
            array[i][j] = 'R'

for i in range(n):
    for j in range(n):
        if visit[i][j] == False:
            visit[i][j] = True
            dfs(i,j)
            rgcnt +=1

print(realcnt,rgcnt)