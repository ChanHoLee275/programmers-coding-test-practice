def num2alpha(x):
    if x == "10":
        return "A"
    elif x == "11":
        return "B"
    elif x == "12":
        return "C"
    elif x == "13":
        return "D"
    elif x == "14":
        return "E"
    elif x == "15":
        return "F"
    else :
        return x
    
def convertor(number, n):
    answer = []
    while number // n != 0:
        answer.append(str(int(number % n)))
        number /= n
    answer.append(str(int(number)))
    answer.reverse()
    answer = list(map(num2alpha, answer))
    return "".join(answer)

def solution(n, t, m, p):
    answer = ''
    start = 0
    string = ''
    while len(string) < t*m:
        string += convertor(start, n)
        start += 1
    for i in range(p-1, t*m, m):
        answer += string[i]
    return answer