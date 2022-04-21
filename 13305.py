#주유소
import sys
n = int(sys.stdin.readline())
dis = list(map(int, sys.stdin.readline().split()))
oil = list(map(int, sys.stdin.readline().split()))
cheap = oil[0]
sum = 0
for i in range(n-1):
    cheap = min(cheap, oil[i])
    sum += cheap * dis[i]
print(sum)