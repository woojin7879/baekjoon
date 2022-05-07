from collections import deque
def solution(rc, operations):
    answer = [[]]
    rn = len(rc)
    an = len(rc[0])
    n = rn * an
    actual = []
    for i in rc:
        for j in i:
            actual.append(j)
    coor = [i for i in range(n)]
    for o in operations:
        if o == "ShiftRow":
            for i in range(n):
                coor[i] += an
                coor[i] %= n
        elif o == "Rotate":
            for i in range(n):
                if coor[i] % an == (an - 1) and coor[i] != (an - 1):
                    coor[i] -= an
                    coor[i] %= n
                elif coor[i] % an == 0 and coor[i] != (n - an):
                    coor[i] += an
                    coor[i] %= n
                elif coor[i] < an and coor[i] > 0:
                    coor[i] -= 1
                elif coor[i] < (n - 1) and coor[i] > (n - an - 1):
                    coor[i] += 1
    new = [[0 for _ in range(an)] for _ in range(rn)]
    for i in range(rn):
        for j in range(an):
            new[i][j] = actual[coor[rn * i + j]]
    print(new)
    return new
solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ["Rotate","Rotate","Rotate","Rotate","Rotate","Rotate","Rotate","Rotate"])