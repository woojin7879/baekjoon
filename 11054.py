#가장 긴 바이토닉 부분 수열
import sys
a = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
reverse = array[::-1] #by slicing
ascend = [1] * a
descend = [1] * a
maxnum = 1
for i in range(a):
    for j in range(i):
        if array[j] < array[i]:
            ascend[i] = max(ascend[i], ascend[j] + 1)
        if reverse[j] < reverse[i]:
            descend[i] = max(descend[i], descend[j] + 1)

for i in range(a):
    maxnum = max(maxnum, ascend[i] + descend[a-i-1] - 1)
print(maxnum)