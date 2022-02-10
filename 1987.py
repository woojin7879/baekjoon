#알파벳
import sys
r, c = map(int,sys.stdin.readline().split())
array = []
for _ in range(r):
    array.append(list(map(str, sys.stdin.readline().rstrip())))
dx = [0,0,1,-1]
dy = [1,-1,0,0]
cnt = 0
visit = [0] * 26
def alpha(x,y,count):
    global cnt
    for i in range(4):
        a = x + dx[i]
        b = y + dy[i]
        cnt = max(cnt,count)
        if ((0 <= a < r) & (0 <= b < c)):
            if visit[ord(array[a][b])-65] == 0:
                visit[ord(array[a][b])-65] = 1
                alpha(a,b,count+1)
                visit[ord(array[a][b])-65] = 0
visit[ord(array[0][0])-65] = 1
alpha(0,0,1)
print(cnt)

# 처음에 in을 써서 시간초과가 많이난것같다 알파벳 크기의 리스트를 선언해 관리해 시간초과를 해결했다. 
# in은 리스트를 순회해 시간복잡도가 O(n)이라한다.