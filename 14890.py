#경사로
import sys
n, l = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
road = 0
for i in range(n):
    tmp = graph[i][0]
    cnt = 1
    flag = True
    for j in range(1, n):
        if tmp == graph[i][j]:
            cnt += 1
        elif tmp - graph[i][j] == 1 and cnt >= 0:
            cnt = 1 - l
        elif tmp - graph[i][j] == -1 and cnt >= l:
            cnt = 1
        else:
            flag = False
            break
        tmp = graph[i][j]
    if flag and cnt >= 0:
        road += 1
for j in range(n):
    tmp = graph[0][j]
    cnt = 1
    flag = True
    for i in range(1, n):
        if tmp == graph[i][j]:
            cnt += 1
        elif tmp - graph[i][j] == 1 and cnt >= 0:
            cnt = 1 - l
        elif tmp - graph[i][j] == -1 and cnt >= l:
            cnt = 1
        else:
            flag = False
            break
        tmp = graph[i][j]
    if flag and cnt >= 0:
        road += 1
print(road)

