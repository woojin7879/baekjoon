#합분해
import sys
import math
n, k = map(int, sys.stdin.readline().split())
print(((math.factorial(n + k - 1) // (math.factorial(k - 1) * math.factorial(n)))%1000000000))