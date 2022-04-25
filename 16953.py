#A->B
import sys
from collections import deque
a, b = map(int, sys.stdin.readline().split())
deq = deque()
deq.append([a, 1])
ans = -1
while deq:
    n , t = deq.popleft()
    temp1 = n * 2
    temp2 = n * 10 + 1
    if temp1 == b or temp2 == b:
        ans = t + 1
        break
    if temp1 < b:
        deq.append([temp1, t + 1])
    if temp2 < b:
        deq.append([temp2, t + 1])
print(ans)