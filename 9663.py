#N-Queen 문제
a = int(input())

array = [0]*a
num = 0

def queen(k):
    global num
    if(k==a):
        num += 1
        return  
    for i in range(0,a):
        array[k] = i
        if (possible(k)):
            queen(k+1)

def possible(l):
    for j in range(0,l):
        if (((array[l]+l)==(array[j]+j)) | ((array[l]-array[j])==(l-j)) | (array[l]==array[j])):
            return False
    return True

queen(0)
print(num)
