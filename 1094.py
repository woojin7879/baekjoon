#막대기
import sys
n = int(sys.stdin.readline())
num = 64
sum = 0
while n != 0:
    tmp = n // num
    sum += tmp
    n -= (num * tmp)
    num //= 2
print(sum)