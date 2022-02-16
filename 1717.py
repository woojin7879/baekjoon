#집합의 표현
import sys
sys.setrecursionlimit(10**6)
n, m = map(int, sys.stdin.readline().split())
original = [i for i in range(n+1)]

def find(x):
    if x == original[x]:
        return x
    other = find(original[x])
    original[x] = other
    return other

def union(x,y):
    x = find(x)
    y = find(y)
    if x < y:
        original[y] = x
    else:
        original[x] = y

for i in range(m):
    o , a, b = map(int, sys.stdin.readline().split())
    if o == 0:
        union(a,b)
    else:
        if find(a) ==  find(b):
            print("YES")
        else:
            print("NO")