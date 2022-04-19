#로프
import sys
n = int(sys.stdin.readline())
rope = []
for _ in range(n):
    rope.append(int(sys.stdin.readline()))
rope.sort()
sum = 0
for i in range(1, n + 1):
    sum = max(sum, i * rope[n - i])
print(sum)