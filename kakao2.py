from collections import deque
def solution(queue1, queue2):
    answer = -1
    q1 = sum(queue1)
    q2 = sum(queue2)
    d1 = deque(queue1)
    d2 = deque(queue2)
    sumq = q1 + q2
    while (answer <= 4 * len(queue1)):
        answer += 1
        if q1 < q2:
            a = d2.popleft()
            q2 -= a
            q1 += a
            d1.append(a)
        elif q1 > q2:
            a = d1.popleft()
            q1 -= a
            q2 += a
            d2.append(a)
        else:
            return answer
            break
    return -1