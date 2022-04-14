#PPAP
import sys
s = list(map(str, sys.stdin.readline().strip()))
stack = []
for i in range(len(s)):
    stack.append(s[i])
    if stack[-4:] == ['P', 'P', 'A', 'P']:
        stack.pop()
        stack.pop()
        stack.pop()
if stack == ['P', 'P', 'A', 'P'] or stack == ['P']:
    print("PPAP")
else:
    print("NP")