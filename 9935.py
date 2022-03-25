#문자열 폭발
import sys
word = sys.stdin.readline().strip()
bomb = sys.stdin.readline().strip()
stack = []
for i in word:
    stack.append(i)
    if i == bomb[-1] and ''.join(stack[-len(bomb):]) == bomb:
        del stack[-len(bomb):]
if stack: 
    print(''.join(stack)) 
else: 
    print("FRULA")

#신기한 생각 방식을 알아간다.