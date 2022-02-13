#테트로미노
from collections import deque
import sys
n, m = map(int, sys.stdin.readline().split())
array = []
visit = [[0]*m for _ in range(n)]
for _ in range(n):
    array.append(list(map(int, sys.stdin.readline().split())))

dx = [0,0,1,-1]
dy = [1,-1,0,0]
maxnum = 0
def dfs(x,y,cnt,num):
    visit[x][y] = 1
    if cnt == 1 or cnt == 3:
        for i in range(4):
            a = x + dx[i] 
            b = y + dy[i]
            if ((0 <= a < n) & (0 <= b < m)):
                if (visit[a][b] == 0):
                    dfs(a,b,cnt+1,num + array[a][b])
    elif cnt == 2:
        for i in range(4):
            for j in range(i+1,4):
                a = x + dx[i] 
                b = y + dy[i]
                c = x + dx[j]
                d = y + dy[j]
                if ((0 <= a < n) & (0 <= b < m) & (0 <= c < n) & (0 <= d < m)):
                    if (visit[a][b] == 0) & (visit[c][d] == 0):
                        dfs(a,b,cnt+2,num + array[a][b] + array[c][d])
        for i in range(4):
            a = x + dx[i] 
            b = y + dy[i]
            if ((0 <= a < n) & (0 <= b < m)):
                if (visit[a][b] == 0):
                    dfs(a,b,cnt+1,num + array[a][b])
    elif cnt == 4:
        global maxnum
        maxnum = max(maxnum, num)
    visit[x][y] = 0

for i in range(n):
    for j in range(m):
        dfs(i,j,1,array[i][j])

print(maxnum)