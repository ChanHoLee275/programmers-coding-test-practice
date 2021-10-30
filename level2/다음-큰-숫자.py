def checkNumberOfOne(number1, number2):
    number1 = str(bin(number1))
    number2 = str(bin(number2))
    count1 = 0
    count2 = 0
    for i in list(number1):
        if i == "1":
            count1 += 1
    for i in list(number2):
        if i == "1":
            count2 += 1
    if count1 == count2:
        return True
    else :
        return False

def solution(n):
    answer = n + 1
    while not checkNumberOfOne(n, answer):
        answer += 1
    return answer