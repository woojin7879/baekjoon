#다리 놓기
import sys
import math
t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    dif = m - n
    if dif == 0:
        print(1)
    else:
        print(math.factorial(m)//(math.factorial(n) * math.factorial(dif)))
