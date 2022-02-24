#타일 채우기
import sys
n = int(sys.stdin.readline())
tile = [0] * 31
tile[0] = 1
for i in range(2,n+1,2):
    tile[i] = tile[i-2] * 3
    for j in range(0, i-2, 2):
        tile[i] += tile[j] * 2
print(tile[n])