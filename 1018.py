#체스판 다시 칠하기
import sys
n, m = map(int, sys.stdin.readline().split())
chess = []
for _  in range(n):
    chess.append(list(map(str, sys.stdin.readline().strip())))
ans = 32
for a in range(n -7):
    for b in range(m-7):
        sum = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i + j) % 2 == 1 and chess[i][j] == 'W':
                    sum += 1
                if (i + j) % 2 == 0 and chess[i][j] == 'B':
                    sum += 1
        if sum > 32:
            sum = 64 - sum
        ans = min(ans, sum)
print(ans)