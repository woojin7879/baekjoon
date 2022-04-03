#보물
import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
a.sort()
b.sort()
sum = 0
for i in range(n):
    sum += a[i] * b[n - 1 - i]
print(sum)