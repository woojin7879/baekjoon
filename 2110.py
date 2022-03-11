#공유기 설치 파이썬
import sys
n, c = map(int, sys.stdin.readline().split())
house = []
for _ in range (n):
    house.append(int(sys.stdin.readline()))
house.sort()
start, end = 1, house[-1] - house[0]

while start <= end:
    median = (start + end) // 2
    count = 1
    temp = house[0]
    for i in range(n):
        if house[i] - temp >= median:
            count += 1
            temp = house[i]
    if count >= c:
        result = median
        start = median + 1
    else:
        end = median - 1
print(result)

#이거 거리로 이분탐색 생각을 어떻게 하지