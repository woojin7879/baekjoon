#회의실 배정
import sys
n = int(sys.stdin.readline())
lecture = []
for _ in range(n):
    lecture.append(list(map(int, sys.stdin.readline().split())))
lecture.sort(key=lambda x: (x[1], x[0]))
sum = 1
finish = lecture[0][1]
for i in lecture[1:]:
    if i[0] >= finish:
        finish = i[1]
        sum += 1
print(sum)