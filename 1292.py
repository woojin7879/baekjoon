#쉽게푸는 문제
import sys
a, b = map(int, sys.stdin.readline().split())
num = []
for i in range(b + 1):
    for j in range(i):
        num.append(i)
    if len(num) > b:
        break
print(sum(num[a-1:b]))