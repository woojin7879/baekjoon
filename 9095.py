#1, 2, 3 더하기
import sys
n = int(sys.stdin.readline())
w = [0] * 11
w[1] = 1
w[2] = 2
w[3] = 4
for i in range(4,11):
    w[i] = w[i - 1] + w[i - 2] + w[i - 3]
for i in range(n):
    a = int(sys.stdin.readline())
    print(w[a])