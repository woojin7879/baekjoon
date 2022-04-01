#곱셈
import sys
a, b, c = map(int, sys.stdin.readline().split())
a = a % c
def multiply(x, y):
    if y % 2 == 0:
        return (multiply(x, y//2) ** 2) % c
    elif y == 1:
        return x % c
    else:
        return ((multiply(x, y//2) ** 2) * x) % c
print(multiply(a, b))