#N과 M (1)
import sys
n, m = map(int, sys.stdin.readline().split())
s = []
def dfs(f):
    if len(f) == m:
        print(' '.join(map(str, s)))
        return 
    for i in range(1, n + 1):
        if i not in f:
            f.append(i)
            dfs(f)
            f.pop()
dfs(s)