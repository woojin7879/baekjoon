#감소하는 수
import sys
from collections import deque
n = int(sys.stdin.readline())
num = 9
if n < 10:
    print(n)
else:
    q = deque()
    for i in range(0,10):
        q.append(i)
    while q:
        p = q.popleft()
        for i in range(0, 10):
            if (p % 10) <= i:
                break
            q.append(p*10+i)
            num += 1
            if num == n:
                print(q[-1])
                exit(0)
    print(-1)