#수들의 합
import sys
n = int(sys.stdin.readline())
sum = 0
for i in range(n + 1):
    sum += i
    if sum > n:
        print(i - 1)
        break
    elif sum == n:
        print(i)
        break