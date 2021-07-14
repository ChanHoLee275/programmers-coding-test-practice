# test case 10, 11을 통과하지 못함. 이는 시간이 오래 걸려서 그러는 것이므로, 이에 대한 최적화 필요

def compare(item1,item2):
    count = 0
    item1 = item1[::-1]
    item2 = item2[::-1]
    if len(item1) > len(item2):
        for i in range(len(item1)):
            if i < len(item2) and item1[i] != item2[i]:
                count += 1
            elif i >= len(item2):
                if item1[i] != "0":
                    count += 1
    elif len(item1) == len(item2):
        for i in range(len(item1)):
            if item1[i] != item2[i]:
                count += 1
    else :
        for i in range(len(item2)):
            if i < len(item1) and item1[i] != item2[i]:
                count += 1
            elif i >= len(item1):
                if item2[i] != "0":
                    count += 1
    return count

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        item = numbers[i]
        bin_item = list(bin(item)[2:])
        addition = 1
        while True:
            diff = compare(bin_item,list(bin(item+addition)[2:]))
            if diff <= 2:
                answer.append(item + addition)
                break
            else :
                addition += 1
        
    return answer