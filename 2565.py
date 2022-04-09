#전깃줄
import sys
n = int(sys.stdin.readline())
e = []
for _ in range(n):
    e.append(list(map(int, sys.stdin.readline().split())))
e.sort()
len = [1] * (n)
for i in range(n):
    for j in range(i):
        if e[i][1] > e[j][1]:
            len[i] = max(len[i], len[j] + 1)
print(n - max(len))