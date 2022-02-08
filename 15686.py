#치킨 배달
import sys
from collections import deque
from itertools import combinations
n, m = map(int, sys.stdin.readline().split())
array = []
home = 0
chicken = 0
homearray = deque()
chickenarray = deque()
for i in range(n):
    array.append(list(map(int, sys.stdin.readline().split())))
    home += array[i].count(1)
    chicken += array[i].count(2)

dis = [[0]*home for i in range(chicken)]

for i in range(n):
    for j in range(n):
        if array[i][j] == 1:
            homearray.append([i,j])
        elif array[i][j] == 2:
            chickenarray.append([i,j])
hnum = 0
while homearray:
    x,y = homearray.popleft()
    cnum = 0
    for i in chickenarray:
        dis[cnum][hnum] = abs(x-i[0]) + abs(y-i[1])
        cnum += 1
    hnum += 1
combi = []
for i in range(chicken):
    combi.append(i)
chicken_combi = list(combinations(combi,m))
sumnum = 100*200
for i in chicken_combi:
    result = [100]*home
    for j in range(m):
        for k in range(home):
            result[k] = min(result[k],dis[i[j]][k])
    sumnum = min(sumnum, sum(result))

print(sumnum)