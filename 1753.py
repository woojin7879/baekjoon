#최단경로
#heapq 이용
import heapq
import sys
v, e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
array = [[] for _ in range(v+1)] #v가 아니라 e로해서 런타임 에러남;;;
for _ in range(e):
    a, b, w = (list(map(int, sys.stdin.readline().split()))) #메모리를 줄이는 방법
    array[a].append([b,w]) #a를 저장하지 않아도됨

minway = [10*e+1]*(v+1)
minway[k] = 0
heap = []
heapq.heappush(heap,[0,k])

while heap:
    dis, node = heapq.heappop(heap)
    if minway[node] < dis:
        continue
    for i in array[node]:
        if minway[i[0]] > (dis + i[1]):
            minway[i[0]] = dis + i[1]
            heapq.heappush(heap,[minway[i[0]],i[0]])

for i in range(1,v+1):
    if(minway[i]!=10*e+1):
        print(minway[i])
    else:
        print("INF")