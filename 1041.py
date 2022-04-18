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
ans = 0
ans += min1 * n1
ans += min2 * n2
ans += min3 * n3
if n > 1:
    print(ans)
else:
    ans = sum(dice) - max(dice)
    print(ans)