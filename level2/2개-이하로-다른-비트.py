def diff(number):
    target = list(bin(number)[2:])[::-1]
    target.append("0")
    for i in range(len(target) - 1):
        part = "".join(target[i:i+2])
        if part == "00":
            target[i] = "1"
            return "".join(target[::-1])
        elif part == "01":
            target[i] = "1"
            return "".join(target[::-1])
        elif part == "10":
            target[i] = "0"
            target[i+1] = "1"
            return "".join(target[::-1])
            

def solution(numbers):
    answer = []
    for i in numbers:
        answer.append(int(diff(i),2))
    return answer