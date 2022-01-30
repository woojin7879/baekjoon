#피보나치 문제
a = int(input())

def calculate(k):
    array = [[0]*(2) for l in range(max(k+1,2))]
    array[0][0]=1
    array[0][1]=0
    array[1][0]=0
    array[1][1]=1
    if (k>=2):
        for j in range(2,k+1):
            array[j][0]=array[j-1][0]+array[j-2][0]
            array[j][1]=array[j-1][1]+array[j-2][1]
        print("%d %d"%(array[k][0], array[k][1]))
    elif k==1:
        print("%d %d"%(array[1][0], array[1][1]))
    elif k==0:
        print("%d %d"%(array[0][0], array[0][1]))

for i in range (a):
    b = int(input())
    calculate(b)
