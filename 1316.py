#그룹 단어 체커
import sys
n = int(sys.stdin.readline())
sum = 0
for _ in range (n):
    stack = []
    w = list(map(str, sys.stdin.readline().strip()))
    flag = True
    if len(w) > 1:
        tmp = w[0]
        stack.append(w[0])
        for i in range(1, len(w)):
            if w[i] != tmp:
                if w[i] in stack:
                    flag = False
                    break
                else:
                    stack.append(w[i])
                    tmp = w[i]
    if flag:
        sum += 1
print(sum)