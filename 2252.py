#줄 세우기
import sys
from collections import deque
n, m =  map(int, sys.stdin.readline().split())
link = [0] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = list(map(int, sys.stdin.readline().split()))
    graph[a].append([b])
    link[b] += 1
deq = deque()
for i in range(1,n+1):
    if link[i] == 0:
        deq.append(i)

while deq:
    d = deq.popleft()
    print(d, end = ' ')

    for i in graph[d]:
        for j in range(len(i)):
            link[i[j]] -= 1
            if link[i[j]] == 0:
                deq.append(i[j])

#위상정렬 이용 간선 0인거 큐에계속 순서로 삽입하는 방식