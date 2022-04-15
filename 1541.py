#잃어버린 괄호
import sys
formula = sys.stdin.readline().split('-')
sum = 0
for i in formula[0].split('+'):
    sum += int(i)
for i in formula[1:]: 
    for j in i.split('+'):
        sum -= int(j)
print(sum)
