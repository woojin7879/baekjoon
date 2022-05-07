
def solution(survey, choices):
    answer = ''
    result = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    for i in range(len(survey)):
        result[survey[i][1]] += choices[i] - 4
    if result['R'] < result['T']:
        answer += 'T'
    else:
        answer += 'R'
    if result['C'] < result['F']:
        answer += 'F'
    else:
        answer += 'C'
    if result['J'] < result['M']:
        answer += 'M'
    else:
        answer += 'J'
    if result['A'] < result['N']:
        answer += 'N'
    else:
        answer += 'A'
    return answer