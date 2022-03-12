#센서
import sys
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
sensor = list(map(int, sys.stdin.readline().split()))
sensor.sort()
if k >= n:
    print(0)
else:
    distance = []
    for i in range(0, n-1):
        distance.append(sensor[i + 1] - sensor[i])
    distance.sort()
    for i in range(k-1):
        distance.pop(n - 2 - i)
    print(sum(distance))