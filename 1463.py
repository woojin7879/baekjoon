#1로 만들기
import sys
n = int(sys.stdin.readline())
cost = [0] * (n+1)
cost[1] = 0
for i in range(2, n+1):
    cost[i] = cost[i - 1] + 1
    if i % 3 == 0:
        cost[i] = min(cost[i], cost[i // 3] + 1)
    if i % 2 == 0:
        cost[i] = min(cost[i], cost[i // 2] + 1)
print(cost[n])