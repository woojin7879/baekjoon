#암호 만들기
import sys
l, c = map(int, input().split())
array = sorted(list(map(str, sys.stdin.readline().split())))

def pick(p,item,vowel,consonant):
    if (l-len(item)>c-p):
        return
    if (len(item)==l) & (vowel>=1) & (consonant>=2):
        print(item)
        return
    for i in range (p,c):
        if array[i] in ['a','e','i','o','u']:
            pick(i+1,item+array[i],vowel+1,consonant)
        else:
            pick(i+1,item+array[i],vowel,consonant+1)

pick(0,'',0,0)