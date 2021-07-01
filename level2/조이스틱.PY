def minimum(a,b):
    if a > b:
        return b
    else :
        return a
    
def solution(name):
    if len(name) == 1:
        return ord(name) - ord("A")
    answer = len(name)*"A"
    answer1 = 0
    # 각 위치에 대해서 변화가 필요한 부분인지를 확인
    
    index = list()
    
    for i in range(len(name)):
        if name[i] != answer[i]:
            index.append(i)
    
    # 각 위치 중 현재의 위치에서 이동하는 것 + 문자를 바꾸는 것 중 가장 그 움직임이 적게 드는 것을 계산하고 변화
    
    count = list()

    for i in range(len(index)):
        count.append(minimum(ord(name[index[i]]) - ord("A"), ord("Z") - ord("A") + 1 - (ord(name[index[i]]) - ord("A"))))
    
    moves = 0
    now_index = 0
    while index:
        candidate = list()
        for i in range(len(index)):
            candidate.append(minimum(abs(index[i] - now_index),len(name) - abs(index[i] - now_index)))
        moves += min(candidate)
        next_index = candidate.index(min(candidate))
        now_index = index[next_index]
        del index[next_index]
    
    return sum(count) + moves