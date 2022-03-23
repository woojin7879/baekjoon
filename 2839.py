#설탕 배달
import sys
n = int(sys.stdin.readline())
fresult = n % 5
sum = n // 5
flag = False
while fresult <= n:
    if fresult % 3 == 0:
        flag = True
        sum += fresult // 3
        break
    else:
        fresult += 5
        sum -= 1
if flag:
    print(sum)
else:
    print(-1)