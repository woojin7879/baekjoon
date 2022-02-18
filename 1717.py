#집합의 표현
import sys
sys.setrecursionlimit(100000)
n, m = map(int, sys.stdin.readline().split())
original = [i for i in range(n+1)]

def find(x):
    if x == original[x]:
        return x
    original[x] = find(original[x])
    return original[x]

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
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")

#recursion limit 너무 풀면 메모리 초과 나느듯
#이 문제는 잘모르겠어서 인터넷을 많이 참고했다. 신기한 방식을 배운것 같다.