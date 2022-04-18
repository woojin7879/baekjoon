#주사위
import sys
n = int(sys.stdin.readline())
dice = list(map(int, sys.stdin.readline().split()))
mindice = []
mindice.append(min(dice[0],dice[5]))
mindice.append(min(dice[1],dice[4]))
mindice.append(min(dice[2],dice[3]))
mindice.sort()
min1 = mindice[0]
min2 = mindice[0] + mindice[1]
min3 = sum(mindice)
n1 = 4 * (n - 2) * (n - 1) + (n - 2) ** 2
n2 = 4 * (n - 1) + 4 * (n - 2)
n3 = 4
sum = 0
sum += min1 * n1
sum += min2 * n2
sum += min3 * n3
print(sum)