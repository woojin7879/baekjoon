#소수찾기
from math import sqrt
import sys
n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
sum = 0
for i in num:
    flag = True
    for j in range(2,int(sqrt(i))+1):
        if i % j == 0:
            flag = False
    if flag and i > 1:
        sum += 1
print(sum)