#명령프롬프트
import sys
n =  int(sys.stdin.readline())
first = list(map(str, sys.stdin.readline().strip()))
for i in range(n-1):
    next = list(map(str, sys.stdin.readline().strip()))
    for j in range(len(first)):
        if first[j] != next[j]:
            first[j] = '?'
print("".join(first))