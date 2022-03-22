#2048 (Easy)
import sys
from copy import deepcopy
n = int(sys.stdin.readline())
first = []
for _ in range(n):
    first.append(list(map(int, sys.stdin.readline().split())))
def up(board):
    for j in range(n):
        flag = 0
        for i in range(1,n):
            if board[i][j]:
                temp = board[i][j]
                board[i][j] = 0
                if board[flag][j] == 0:
                    board[flag][j] = temp
                elif board[flag][j] == temp:
                    board[flag][j] *= 2
                    flag += 1
                else:
                    flag += 1
                    board[flag][j] = temp
    return board
def down(board):
    for j in range(n):
        flag = n - 1
        for i in range(n-2, -1, -1):
            if board[i][j]:
                temp = board[i][j]
                board[i][j] = 0
                if board[flag][j] == 0:
                    board[flag][j] = temp
                elif board[flag][j] == temp:
                    board[flag][j] *= 2
                    flag -= 1
                else:
                    flag -= 1
                    board[flag][j] = temp
    return board
def left(board):
    for i in range(n):
        flag = 0
        for j in range(1, n):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                if board[i][flag] == 0:
                    board[i][flag] = tmp
                elif board[i][flag]  == tmp:
                    board[i][flag] *= 2
                    flag += 1
                else:
                    flag += 1
                    board[i][flag]= tmp
    return board
def right(board):
    for i in range(n):
        flag = n - 1
        for j in range(n-2, -1, -1):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                if board[i][flag] == 0:
                    board[i][flag] = tmp
                elif board[i][flag]  == tmp:
                    board[i][flag] *= 2
                    flag -= 1
                else:
                    flag -= 1
                    board[i][flag]= tmp
    return board
answer = 0
def dfs(b, count):
    global answer
    if count == 5:
        answer = max(answer, max(map(max, b)))
    else:
        dfs(up(deepcopy(b)), count + 1)
        dfs(down(deepcopy(b)), count + 1)
        dfs(left(deepcopy(b)), count + 1)
        dfs(right(deepcopy(b)), count + 1)

dfs(first, 0)
print(answer)