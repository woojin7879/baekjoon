#한수
import sys
n = int(sys.stdin.readline())
sum = 99
if n < 100:
    print(n)
else:
    for i in range (100, n + 1):
        if (i // 100) + (i % 10) == (((i % 100) // 10) * 2):
            sum += 1
    print(sum)