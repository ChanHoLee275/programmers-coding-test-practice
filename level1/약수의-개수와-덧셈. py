def function(number):
    
    count = 0
    
    for i in range(1,number+1):
        if number % i == 0:
            count += 1
    
    if count % 2 == 0:
        return number
    else :
        return -1 * number

def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        answer += function(i)
    return answer