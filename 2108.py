#통계학
import sys
from collections import Counter
n = int(sys.stdin.readline())
num = []
for _ in range(n):
    num.append(int(sys.stdin.readline()))
num.sort()
print(round(sum(num)/n))
print(num[n//2])
countnum = Counter(num).most_common()
if len(countnum) > 1 and countnum[0][1] == countnum[1][1]:
    print(countnum[1][0])
else:
    print(countnum[0][0])
print(num[-1]-num[0])