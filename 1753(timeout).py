#최단경로
import sys
v, e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
array = []
for i in range(0, e):
    array.append(list(map(int, sys.stdin.readline().split())))

minway = [11*e]*v
minway[k-1] = 0

def findmin(f,length):
    global minway
    for i in range(0,e):
        if array[i][0] == f:
            minway[array[i][1]-1] = min(length+array[i][2],minway[array[i][1]-1])
            if minway[array[i][1]-1] == length+array[i][2]:
                findmin(array[i][1],minway[array[i][1]-1])

findmin(k,0)
for i in range(0,v):
    if(minway[i]!=11*e):
        print(minway[i])
    else:
        print("INF")

"""
답은 제데로 출력되는데 채점시 시간초과가 난다. 포문을 통해 너무 많은 케이스를 조사하는 것 같다.
찾아보니 heapq라는 시간을 줄여주는 모듈이 있는것같다.
최솟값 순으로 저장 할 수있어 시간의존도를 줄여준다. 
"""
