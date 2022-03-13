#과제
import sys
n = int(sys.stdin.readline())
homework = []
for _ in range(n):
    homework.append(list(map(int, sys.stdin.readline().split())))
homework.sort(reverse = True, key = lambda x: x[1])
day = [0] * (n + 1)
for h in homework:
    for d in range(min(n, h[0]), 0, -1):
        if day[d] == 0:
            day[d] = h[1]
            break
print(sum(day))