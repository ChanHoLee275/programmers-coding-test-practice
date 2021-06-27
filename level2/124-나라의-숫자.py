def ten2three(n):
    answer = list()
    while n:
        answer.append(n%3)
        n = n//3
    return answer

def solution(n):
    answer = ''
    three = ten2three(n)
    for i in range(len(three)):
        if three[i] <= 0 and i < len(three)-1:
            three[i] += 3
            three[i+1] -= 1
    if three[-1] == 0:
        three.pop()
    three = three[::-1]
    for i in three:
        if i == 3:
            answer += '4'
        else :
            answer += str(i)
    return answer