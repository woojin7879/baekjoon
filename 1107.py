#리모컨
from math import inf
import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
remote = []
if m != 0:
    remote = list(map(int,sys.stdin.readline().split()))
num = 0
cnt = inf
flag = True
def check(c):
    if c >= 0:
        for i in str(c):
            if int(i) in remote:
              return False
    return True

if n == 100:
    print(0)
elif m == 10:
    print(abs(100-n))
else:
    while flag and num<abs(100-n):
        if check(n - num) and (n - num) >= 0:
            cnt = min(len(str(n-num))+num, cnt)
            flag = False
        elif check(n + num):
            cnt = min(len(str(n+num))+num, cnt)
            flag = False
        num += 1
    cnt = min(abs(100-n), cnt)
    print(cnt)