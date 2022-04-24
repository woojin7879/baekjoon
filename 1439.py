#뒤집기
import sys
word = list(map(int, sys.stdin.readline().strip()))
num = 1
temp = word[0]
for i in word:
    if temp != i:
        num += 1
        temp = i
print(num // 2)