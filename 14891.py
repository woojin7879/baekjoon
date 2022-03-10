#톱니바퀴
import sys
from collections import deque
wheel = [[] for _ in range(4)]
for i in range(4):
    wheel[i] = deque(list(map(int, list(sys.stdin.readline().strip()))))
k = int(sys.stdin.readline())
turn = deque()
for _ in range(k):
    a, b = list(map(int, sys.stdin.readline().split()))
    turn.append([a, b, 0])
visit = [0] * 5
while turn:
    num, dir, flag = turn.popleft()
    if num + 1 < 5 and flag >= 0:
        if wheel[num][6] != wheel[num - 1][2]:
            turn.appendleft([num + 1, -dir, flag + 1])
    if num - 1 > 0 and flag <= 0:
        if wheel[num - 1][6] != wheel[num - 2][2]:
            turn.appendleft([num - 1, -dir, flag - 1])
    wheel[num - 1].rotate(dir)
sum = 0
for i in range(4):
    sum += (2 ** i) * wheel[i][0]
print(sum)