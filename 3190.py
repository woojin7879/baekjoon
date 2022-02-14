#뱀
from collections import deque
import sys
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
array = [[0]*n for _ in range(n)]
for _ in range(k):
    ax, ay = map(int, sys.stdin.readline().split())
    array[ax-1][ay-1] = 1
l = int(sys.stdin.readline())
change = [[0,0] for _ in range(l)]
for i in range(l):
    x, c = sys.stdin.readline().split()
    change[i][0] = int(x)
    change[i][1] = c

dx = [0,1,0,-1]
dy = [1,0,-1,0]

deq =  deque()
head = [0,0]
deq.append([0,0])
flag = True
cnt = 0
direction = 0
while flag:
    cnt += 1
    if change[0][0] >= n:
        cnt = n
        break

    nexthead = [0,0]
    nexthead[0] = head[0] + dx[direction]
    nexthead[1] = head[1] + dy[direction]

    if not((0 <= nexthead[0] < n) and (0 <= nexthead[1] < n)):
        break
    if nexthead in deq:
        break

    head = nexthead

    if array[head[0]][head[1]] == 1:
        deq.append([head[0],head[1]])
        array[head[0]][head[1]] = 0
    else:
        deq.append([head[0],head[1]])
        deq.popleft()

    for i in range(l):
        if cnt == change[i][0]:
            if change[i][1] == 'D':
                direction = (direction + 1)%4
            else:
                direction = (direction - 1)%4
            break
print(cnt)