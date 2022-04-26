#신입사원
import sys
t = int(sys.stdin.readline())
for _ in range (t):
    n = int(sys.stdin.readline())
    p = []
    for _ in range(n):
        p.append(list(map(int, sys.stdin.readline().split())))
    p.sort()
    max = p[0][1]
    ans = 1
    for i in p[1:]:
        if max > i[1]:
            ans += 1
            max = i[1]
    print(ans)