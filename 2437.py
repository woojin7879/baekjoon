#저울
import sys
n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
num.sort()
sum = 0
for i in range(n):
    if sum + 1 >= num[i]:
        sum += num[i]
    else:
        break
print(sum+1)

