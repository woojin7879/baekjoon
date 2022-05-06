#컵홀더
import sys
n = int(sys.stdin.readline())
chair = str(sys.stdin.readline())
ll = chair.count('LL')
if ll < 2:
    print(n)
else:
    print(n-ll+1)