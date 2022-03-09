#피보나치 수 3
import sys
n = int(sys.stdin.readline())
a = 0
b = 1
n = n % (15*1000000)
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    for i in range (2,n+1):
        a, b = b % 1000000, (a + b) % 1000000
    print(b % 1000000)

#피사노 주기에 대해 알아야 풀 수 있는 문제