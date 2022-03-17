#거스름돈
import sys
n = int(sys.stdin.readline())
sum = 0
money =  1000 - n
coin = [500,100,50,10,5,1]
for i in range(6):
    sum += money // coin[i]
    money = money % coin[i]
print(sum)