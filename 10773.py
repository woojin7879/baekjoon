#제로
import sys
n = int(sys.stdin.readline())
num = []
for _ in range(n):
    k = int(sys.stdin.readline())
    if k:
        num.append(k)
    else:
        num.pop()
print(sum(num))