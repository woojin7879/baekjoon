#오븐시계
import sys
m, s = map(int, sys.stdin.readline().split())
t = int(sys.stdin.readline())
print((m+(s+t)//60)%24, (s+t)%60)