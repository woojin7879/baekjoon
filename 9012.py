#괄호
import sys
n = int(sys.stdin.readline())
for _ in range(n):
    p = list(map(str, sys.stdin.readline().strip()))
    stack = []
    flag = True
    for i in range(len(p)):
        if p[i] == '(':
            stack.append(p[i])
        else:
            if len(stack) == 0:
                flag = False
                break
            else:
                stack.pop()
    if flag and len(stack) == 0:
        print('YES')
    else:
        print('NO')
