#평범한 배낭
import sys
n, k = map(int,sys.stdin.readline().split())
array=[]
for _ in range(n):
    array.append(list(map(int, sys.stdin.readline().split())))

value = [[0] * (k+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,k+1):
        if j < array[i-1][0]:
            value[i][j]=value[i-1][j]
        else:
            value[i][j] = max(value[i-1][j],value[i-1][j-array[i-1][0]]+array[i-1][1])
print(value[-1][-1])

#처음에 중복 안되는질 몰라서 좀 헤멨다. 질문 보다보니 중복 안되서 value를 이중으로 만들어 아이템 한개씩만 처리했다.