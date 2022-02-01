#Fly me to the Alpha Centauri
import math
a = int(input())

def calculate(k):
    i=0
    a=0
    while i<=k:
        if i**2==k:
            print(2*i-1)
            break
        elif i**2>k:
            a=math.ceil((k-(i-1)**2)/(i-1))
            print(2*i-3+a)
            break
        i += 1

for i in range (a):
    b,c = map(int, input().split())
    calculate(c-b)