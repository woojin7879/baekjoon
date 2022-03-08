#최소비용 구하기
from math import inf
import sys
import heapq
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
bus = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = (list(map(int, sys.stdin.readline().split())))
    bus[a].append([b,c])
s, e = map(int, sys.stdin.readline().split())
heap = []
heapq.heappush(heap, [0, s])
distance = [inf] * (n+1)
distance[s] = 0
while heap:
    money, place = heapq.heappop(heap)
    if distance[place] < money:
        continue
    for end, cost in bus[place]:
        if distance[end] > money + cost:
            distance[end] = money + cost
            heapq.heappush(heap, [distance[end], end])
print (distance[e])