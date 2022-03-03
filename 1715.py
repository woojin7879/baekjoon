#카드 정렬하기
import sys
import heapq
n = int(sys.stdin.readline())
heap = []
for _ in range(n):
    heapq.heappush(heap, int(sys.stdin.readline()))
num = 0
while len(heap)>1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    heapq.heappush(heap, a + b)
    num += a + b
print(num)