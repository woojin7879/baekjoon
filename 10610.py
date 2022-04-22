#30
import sys
num = list(map(int, sys.stdin.readline().strip()))
num.sort(reverse=True)
if num[-1] == 0 and sum(num) % 3 == 0:
    for i in num:
        print(i,end='')
else:
    print(-1)