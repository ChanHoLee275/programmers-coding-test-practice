def divide(x, start):
    if x % start == 0:
        return x / start
    else:
        return x

def solution(arr):
    
    result = []
    
    start = 2
    maximum = max(arr)   
    
    while start <= maximum:
        if len(list(filter(lambda x: x % start == 0, arr))) > 1:
            result.append(start)
            arr = list(map(lambda x: divide(x,start), arr))
        else :
            start += 1

    answer = 1
    
    for i in result:
        answer *= i
    
    for i in arr:
        answer *= i
    
    return answer