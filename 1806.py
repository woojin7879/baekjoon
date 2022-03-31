#부분합
import sys
n, s = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
left, right = 0, 0
sum = 0
minimum = n + 1
while True:
    if sum >= s:
        minimum =  min(minimum, right - left)
        sum -= num[left]
        left += 1
    elif right == n:
        break
    else:
        sum += num[right]
        right += 1
if minimum == n + 1:
    print(0)
else:
    print(minimum)