def solution(citations):
    answer = 0
    citations.sort()
    maximum = max(citations)
    for i in range(maximum):
        count = 0
        for j in range(len(citations)):
            if citations[j] >= i:
                break
            else :
                count += 1
        if len(citations) - count >= i:
            continue
        else :
            return i - 1
    return 0