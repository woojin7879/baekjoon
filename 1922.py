#네트워크 연결
import heapq
import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
heap = []
for _ in range(m):
    a, b, c = (list(map(int, sys.stdin.readline().split()))) #메모리를 줄이는 방법
    heapq.heappush(heap,[c,a,b])
original = [i for i in range(n+1)]
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