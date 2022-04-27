#캠핑
import sys
n = 0
while True:
    n += 1
    l, p, v = map(int, sys.stdin.readline().split())
    if l == 0 and p == 0 and v == 0:
        break 
    sum = 0
    sum += (v // p) * l
    sum += min(l, v%p)
    print('Case %d: %d' %(n, sum))