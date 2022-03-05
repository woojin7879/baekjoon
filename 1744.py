#수묶기
import sys
n = int(sys.stdin.readline())
positive = []
negative = []
sum = 0
for _ in range(n):
    i = int(sys.stdin.readline())
    if i > 1:
        positive.append(i)
    elif i == 1:
        sum += 1
    else:
        negative.append(i)
positive.sort()
negative.sort()
if len(positive) % 2 == 0:
    for i in range(len(positive)-1,0,-2):
        sum += positive[i] * positive[i-1]
else:
    for i in range(len(positive)-1,1,-2):
        sum += positive[i] * positive[i-1]
    sum += positive[0]

if len(negative) % 2 == 0:
    for i in range(0,len(negative),2):
        sum += negative[i] * negative[i+1]
else:
    for i in range(0,len(negative)-1,2):
        sum += negative[i] * negative[i+1]
    sum += negative[len(negative)-1]
print(sum)