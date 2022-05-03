#기타줄
import sys
n, m = map(int, sys.stdin.readline().split())
six = 1000
one = 1000
for _ in range (m):
    s, o = map(int, sys.stdin.readline().split())
    six = min(s, six)
    one = min(o, one)
if (six / 6) > one:
    print(one * n)
else:
    sum = 0
    sum += six * (n // 6)
    if six < (n % 6) * one:
        sum += six
    else:
        sum += (n % 6) * one
    print(sum)