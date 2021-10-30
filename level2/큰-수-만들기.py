# 완전 탐색으로 찾기
import itertools

def solution(number, k):
    return str(max(list(map(lambda x: int(''.join(list(x))), list(itertools.combinations(number, len(number) - k))))))


# 테스트 10, 11 통과 못함
import collections

def solution(number, k):
    numbers = list(map(int, list(number)))
    answer = []
    length = len(numbers) - k
    tails = numbers[-length + 1:]
    tails = collections.deque(tails)
    target = numbers[0:-length + 1]
    while True:
        maximum = max(target)
        answer.append(str(maximum))
        if len(answer) == length:
            break
        if target.index(maximum) + 1 == len(target):
            answer += list(map(str, tails))
            break
        target = target[target.index(maximum)+1:]
        target.append(tails.popleft())
        if len(target) == 1:
            answer.append(str(target[0]))
            answer += list(map(str, tails))
            break

    return ''.join(answer)

# 구글링을 통한 답

def solution(number, k):
    answer = [] # Stack
    
    for num in number:
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)
        
    return ''.join(answer[:len(answer) - k])
            