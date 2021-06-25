def ten2three(n):
    # 뒤집기를 효율적으로 하기 위해서 string을 활용
    answer = ""
    # 10진법을 3진법으로 바꾸는 코드, 지속적으로 나누어서 나머지와 몫으로 표현할 수 있다.
    # 3으로 나눈 몫을 지속적으로 3으로 나누다가, 3으로 나누어 떨어지거나 그보다 값이 작게 되면 더 이상 진행할 수 없는 것이므로 종료
    while n//3 >= 3:
        
        answer += str(n%3)

        n = n//3
    
    answer += str(n%3)
    
    if n//3 != 0:
        
        answer += str(n//3)
    
    answer = answer[::-1]
    
    return answer

def three2ten(n):
    answer = 0
    multi = 1
    # 각 자리수는 1,3,9,27이 곱해진 것을 의미 하므로 multi라는 변수를 한 자리씩 증가할 떄 마다 3씩 곱해주어 10진법의 수로 변환
    for i in range(len(n)):
        answer += int(n[i])*multi
        multi *= 3
    return answer

def solution(n):
    n_three = ten2three(n)
    answer = three2ten(n_three)
    return answer
