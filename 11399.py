#ATM
import sys
n = int(sys.stdin.readline())
time = list(map(int, sys.stdin.readline().split()))
time.sort()
sum = 0
for i in range(n):
    sum += (n - i) * time[i]
print(sum)