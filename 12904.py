#A와 B
import sys
s = str(sys.stdin.readline().strip())
t = str(sys.stdin.readline().strip())
while(len(s) != len(t)):
    if t[-1] == 'A':
        t = t[:-1]
    else:
        t = t[:-1]
        t = t[::-1]
if s == t:
    print(1)
else:
    print(0)