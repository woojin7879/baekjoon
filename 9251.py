#LCS
import sys
a = sys.stdin.readline().strip() #strip 안해주니까 공백까지 받아서 길이 1 더받음
b = sys.stdin.readline().strip()
alen = len(a)
blen = len(b)
maxlen = [[0]*(blen+1) for _ in range(alen+1)]

for i in range(alen):
    for j in range(blen):
        if a[i] == b[j]:
            maxlen[i+1][j+1] = maxlen[i][j] + 1
        else:
            maxlen[i+1][j+1] = max(maxlen[i+1][j],maxlen[i][j+1])
print(maxlen[-1][-1]) #-1은 오른쪽부터 즉 맨끝 숫자