#전자레인지
import sys
t = int(sys.stdin.readline())
if t % 10 != 0:
    print(-1)
else:
    print(t // 300, end = ' ')
    t = t % 300
    print(t // 60, end = ' ')
    t = t % 60
    print(t // 10)