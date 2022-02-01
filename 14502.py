#연구소 문제
from collections import deque
import copy
n, m = map(int, input().split())
array = []
maxzero=0

for i in range(0,n):
    array.append(list(map(int, input().split())))

def wall(w):
    if w == 3:
        virus()
        return
    for i in range(0,n):
        for j in range(0,m):
            if array[i][j] == 0:
                array[i][j] = 1
                wall(w+1)
                array[i][j] = 0

def virus():
    varray = copy.deepcopy(array)
    deq = deque() 
    for i in range(0,n):
        for j in range(0,m):
            if varray[i][j] == 2:
                deq.append([i,j])
    while deq:
        x,y = deq.popleft()
        if varray[x][y] == 2:
            if varray[max(0,x-1)][y] == 0 & x-1 >= 0:
                varray[x-1][y] = 2
                deq.append([x-1,y])
            if varray[x][max(0,y-1)] == 0 & y-1 >= 0:
                varray[x][y-1] = 2
                deq.append([x,y-1])   
            if varray[min(n-1,x+1)][y] == 0 & x+1 <n:
                varray[x+1][y] = 2
                deq.append([x+1,y])
            if varray[x][min(m-1,y+1)] == 0 & y+1 <m:
                varray[x][y+1] = 2
                deq.append([x,y+1])
    cnt=0
    for i in range(0,n):
        cnt += varray[i].count(0)
    global maxzero
    maxzero = max(maxzero,cnt)

wall(0)
print(maxzero)
"""
백준 통과는 했는데 길게 코딩한것 같아 블로그들 염탐해보니 거의 비슷한거같다. 
벽 놓는건 케이스 다조사하는 방법 밖에 없는 듯?
"""
    