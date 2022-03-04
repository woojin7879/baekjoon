#보석 도둑
import sys
import heapq
n, k = map(int, sys.stdin.readline().split())
jewerly = []
bag = []
for _ in range(n):
    m, v = map(int, sys.stdin.readline().split())
    heapq.heappush(jewerly, (m, v))
for _ in range(k):
    heapq.heappush(bag, int(sys.stdin.readline()))
sum = 0
temp = []
for _ in range(k):
    b = heapq.heappop(bag)
    while jewerly and  b >= jewerly[0][0]:
        m, v = heapq.heappop(jewerly)
        heapq.heappush(temp, -v)
    if temp:
        sum -= heapq.heappop(temp)
    elif not jewerly:
        break
print(sum)