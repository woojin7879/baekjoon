#동전 1
import sys
n, k = map(int,sys.stdin.readline().split())
array=[]
for _ in range(n):
    array.append(int(sys.stdin.readline()))
totalnum = [0] * (k+1)
totalnum[0] = 1 #최초 1회 용
for i in array:
    for j in range(i,k+1):
        totalnum[j] += totalnum[j-i]
print(totalnum[-1])