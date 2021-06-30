import itertools

# 너무 오래 걸린다.
# 처음 진행한 방식은 완전 탐색 방식. 하지만 이러한 문제는 너무 시간이 오래 걸린다는 단점이 존재

def solution(numbers):
    
    answer = ''
    
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])
    
    permutation = itertools.permutations(numbers,len(numbers))
    
    permutation = list(permutation)
    candidate = list()
    
    for i in range(len(permutation)):
        string = list(permutation[i])
        number = int(''.join(string))
        candidate.append(number)
        
    
    return max(candidate)

# 수정한 코드
# 1000 이하의 number만 들어오므로, x*3을 통해서, 자릿수가 3개가 되도록 하여 이를 비교

def solution(numbers):
    numbers = list(map(str,numbers))
    numbers.sort(key=lambda x : x*3, reverse=True)
    return str(int(''.join(numbers)))