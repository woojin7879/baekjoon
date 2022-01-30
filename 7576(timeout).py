#토마토 문제
m, n = map(int, input().split())
array = []
farray = [[0]*(m) for _ in range(n)]
tomato = 0
num = 0
asum = 0
zsum = 1
zero = True
flag = True

for i in range(0,n):
    array.append(list(map(int, input().split())))


for i in range(0,n):
    for j in range(0,m):
        farray[i][j]=array[i][j]

while flag == True:
    zsum = 1

    for i in range(0,n):
        for j in range(0,m):
            if array[i][j] == 1:
                if array[max(0,i-1)][j] == 0:
                    farray[max(0,i-1)][j] = 1
                if array[i][max(0,j-1)] == 0:
                    farray[i][max(0,j-1)] = 1
                if array[min(n-1,i+1)][j] == 0:
                    farray[min(n-1,i+1)][j] = 1
                if array[i][min(m-1,j+1)] == 0:
                    farray[i][min(m-1,j+1)] = 1
            zsum *= farray[i][j]
    if zsum != 0:
        zero = False
    if array == farray:
        flag = False
    for i in range(0,n):
        for j in range(0,m):
            array[i][j]=farray[i][j]

    num += 1

if zero == True:
    print(-1)
else:
    print(num-1)

#while 안에 for로 인한 timeout