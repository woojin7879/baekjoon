#정수 삼각형
import sys
n = int(sys.stdin.readline())
tri = []
for _ in range(n):
    tri.append(list(map(int, sys.stdin.readline().split())))
sum = [[0] * (i + 1) for i in range(n)]
sum[0][0] = tri[0][0]
for i in range(1, n):
    sum[i][0] = tri[i][0] + sum[i - 1][0]
    sum[i][i] = tri[i][i] + sum[i - 1][i - 1]
    for j in range(1,i):      
        sum[i][j] = tri[i][j] + max(sum[i-1][j-1], sum[i-1][j])
print(max(sum[n-1]))