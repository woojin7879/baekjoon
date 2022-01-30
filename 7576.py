#토마토 문제
from collections import deque
m, n = map(int, input().split())
array = []
num=1
zero=1
for i in range(0,n):
    array.append(list(map(int, input().split())))

deq = deque() 
for i in range(0,n):
    for j in range(0,m):
        if array[i][j] ==1:
            deq.append([i,j])

while deq:
    x,y = deq.popleft()
    if array[x][y] > 0:
        if array[max(0,x-1)][y] == 0 & x-1 >= 0:
            array[x-1][y] = array[x][y] + 1
            deq.append([x-1,y])   
            num=max(num,array[x-1][y])
        if array[x][max(0,y-1)] == 0 & y-1 >= 0:
            array[x][y-1] = array[x][y] + 1
            deq.append([x,y-1])   
            num=max(num,array[x][y-1])
        if array[min(n-1,x+1)][y] == 0 & x+1 <n:
            array[x+1][y] = array[x][y] + 1
            deq.append([x+1,y])
            num=max(num,array[x+1][y])
        if array[x][min(m-1,y+1)] == 0 & y+1 <m:
            array[x][y+1] = array[x][y] + 1
            deq.append([x,y+1])
            num=max(num,array[x][y+1])

for i in array:
        if 0 in i:
            zero = 0

if zero == 0:
    print(-1)
else:
    print(num-1)

#deque 사용 while로 해결, deque pop 시간복잡도 O(1)
#queue 는 시간 복잡도 O(N)