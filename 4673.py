#셀프넘버
def self(k):
    exist = False
    for j in range(0,k):
        sum = 0
        sum += j + j%10 + int((j%100)/10) + int((j%1000)/100) +int(j/1000)
        if sum == k:
            exist = True
    if not exist:
        print(k)

for i in range(1,10000):
    self(i)