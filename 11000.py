#강의실 배정
import sys
import heapq
n = int(sys.stdin.readline())
lecture = []
for _ in range(n):
    lecture.append(list(map(int, sys.stdin.readline().split())))
lecture.sort()
room = []
heapq.heappush(room, -1)

for l in lecture:
    if l[0] < room[0]:
        heapq.heappush(room, l[1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, l[1])
print(len(room))
