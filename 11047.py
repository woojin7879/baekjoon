#동전 0
import sys
n, k = map(int, sys.stdin.readline().split())
coin = []
for i in range(n):
    coin.append(int(sys.stdin.readline()))
sum = 0
for i in range(n-1,-1,-1):
    sum += k // coin[i]
    k = k % coin[i]
    if k == 0:
        break
print(sum)