def isOne(string):
    if(string == "1"):
        return True
    else :
        return False

def myBinary(s,stack,count):
    target = list(s)
    ones = list(filter(isOne,target))
    count[0] = count[0] + 1
    stack.append(len(target)-len(ones))
    length = len(ones)
    binary = bin(length)[2:]
    return binary
    
def solution(s):
    zeros = []
    target = s
    count = [0];
    while True:
        if(target == "1"):
            break
        target = myBinary(target,zeros,count)
    answer = [count[0], sum(zeros)]
    return answer