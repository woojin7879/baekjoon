#AC
import sys
from collections import deque
t = int(sys.stdin.readline())
for _ in range(t):
    p = sys.stdin.readline()
    n = int(sys.stdin.readline())
    array = sys.stdin.readline()
    if n == 0:
        array = deque()
    else:
        array = deque(array[1:-2].split(','))
    flag = True
    dirflag = False
    for i in p:
        if i == 'R':
            if dirflag:
                dirflag = False
            else:
                dirflag = True
        elif i == "D":
            if len(array) == 0:
                print('error')
                flag = False
                break
            if dirflag:
                array.pop()
            elif not dirflag:
                array.popleft()
    if flag:
        if dirflag:
            array.reverse()
        print("[" + ",".join(array) + "]")