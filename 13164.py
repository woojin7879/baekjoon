#행복유치원
import sys
n, k = map(int, sys.stdin.readline().split())
student = list(map(int, sys.stdin.readline().split()))
difference = []
for i in range(n-1):
    difference.append(student[i + 1] - student[i])
difference.sort()
for i in range(k-1):
    difference.pop()
print(sum(difference))