#2xn 타일링 2
import sys
n = int(sys.stdin.readline())
way = [0] * (n + 1)
way[1] = 1
if n > 1:
    way[2] = 3
for i in range(3, n + 1):
    way[i] = way[i - 1] + 2 * way[i - 2]
print(way[-1] % 10007)