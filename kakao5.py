from collections import deque
def solution(rc, operations):
    answer = [[]]
    r = deque(rc)
    for i in operations:
        if i == "ShiftRow":
            a = r.pop()
            r.appendleft(a)
        elif i == "Rotate":
            temp1 = deque()
            temp2 = deque()
            for i in range(len(r)):
                a = deque(r.popleft())
                if i != 0:
                    temp1.append(a.popleft())
                if i != (len(r)):
                    temp2.append(a.pop())
                r.append(list(a))
            for i in range(len(r)):
                a = deque(r.popleft())
                if i != (len(r)):
                    a.appendleft(temp1.popleft())
                if i != 0:
                    a.append(temp2.popleft())
                r.append(list(a))
    return list(r)