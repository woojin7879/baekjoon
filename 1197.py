#최소 스팬닝 트리
import heapq
import sys
v, e = map(int, sys.stdin.readline().split())
heap = []
for _ in range(e):
    a, b, c = (list(map(int, sys.stdin.readline().split()))) #메모리를 줄이는 방법
    heapq.heappush(heap,[c,a,b])
original = [i for i in range(v+1)]
def find(x):
    if x == original[x]:
        return x
    original[x] = find(original[x])
    return original[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x < y:
        original[y] = x
    else:
        original[x] = y

def kruskal():
    num = 0
    while heap:
        dis, x, y = heapq.heappop(heap)
        if find(x) != find(y):
            num += dis
            union(x,y)
    print(num)

kruskal()

#크루스컬 알고리즘을 find union알고리즘을 이용해 구현하였다.