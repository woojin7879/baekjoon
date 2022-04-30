#AB
from re import A
import sys
n, k = map(int, sys.stdin.readline().split())
sum = 0
a = []
t = 0
for i in range(n):
    if sum + n - 1 - i - t < k:
        a.append(i)
        sum += n - 1 - i - t
        t += 1
    elif sum + n - 1 - i - t == k:
        sum += n - 1 - i - t
        a.append(i)
        break
if sum == k:
    for i in range(n):
        if i in a:
            print("A",end='')
        else:
            print("B",end='')
else:
    print(-1)