#단어 수학
import sys
n = int(sys.stdin.readline())
word = {}
for _ in range(n):
    a = list(map(str, sys.stdin.readline().rstrip()))
    for i in range(len(a)):
        if a[i] in word:
            word[a[i]] += 10 ** (len(a) - i - 1)
        else:
            word[a[i]] = 10 ** (len(a) - i - 1)
sortword = sorted(word.items(), key = lambda item: item[1], reverse = True)
num = 9
sum = 0
for val in sortword:
    sum += val[1] * num
    num -= 1
print(sum)