#주사위 굴리기
import sys
n, m, x, y, k = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
move = list(map(int, sys.stdin.readline().split()))
dice = [0] * 6
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(k):
    dir = move[i]-1
    a = x + dx[dir]
    b = y + dy[dir]
    if (0 <= a < n) and (0 <= b < m):
        if dir == 0:
            dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
        elif dir == 1:
            dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
        elif dir == 2:
            dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
        else:
            dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
        if graph[a][b] == 0:
            graph[a][b] = dice[5]
        else:
            dice[5] = graph[a][b]
            graph[a][b] = 0
        x, y = a, b
        print(dice[0])