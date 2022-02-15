#스도쿠
import sys
array = []
for _ in range(9):
    array.append(list(map(int, sys.stdin.readline().split())))
blank = []
for i in range(9):
    for j in range(9):
        if array[i][j] == 0:
            blank.append([i,j])

def checkrow(x, num):
    for i in range(9):
        if array[x][i] == num:
            return False
    return True

def checkcolumn(y, num):
    for i in range(9):
        if array[i][y] == num:
            return False
    return True

def checkbox(x,y,num):
    for i in range(x-x%3,x-x%3+3):
        for j in range(y-y%3,y-y%3+3):
            if array[i][j] == num:
                return False
    return True

def dfs(cnt):
    if cnt == len(blank):
        for i in range(9):
            print(*array[i])
        sys.exit()
    x = blank[cnt][0]
    y = blank[cnt][1]
    for i in range(1,10):
        if checkrow(x,i) and checkcolumn(y,i) and checkbox(x,y,i):
            array[x][y] = i
            dfs(cnt+1)
            array[x][y] = 0

dfs(0)