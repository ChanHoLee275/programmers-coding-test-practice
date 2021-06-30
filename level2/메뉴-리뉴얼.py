<<<<<<< HEAD
def solution(orders, course):
    answer = []
    
    # split orders
    
    for i in range(len(orders)):
        orders[i] = list(orders[i])
    
    frequentitem = dict()
    
    # finding frequent item
    for i in range(len(orders)):
        for j in range(len(orders[i])):
            if orders[i][j] in frequentitem.keys():
                frequentitem[orders[i][j]] += 1
            else :
                frequentitem[orders[i][j]] = 1
    
    delete = list()

    for i in frequentitem.keys():
        if frequentitem[i] == 1:
            delete.append(i)
    
    for i in range(len(delete)):
        del frequentitem[delete[i]]
    
    print(frequentitem)

    while True:
        # find frequentitem
        candidate = list()
        keys = frequentitem.keys()
        for i in range(len(keys)):
            for j in range(len(keys)):
                if i != j:
                    candidate.append(keys[i] + keys[j])
        
        # checking frequent
        frequent = [0]*len(candidate)
        
        for i in range(len(orders)):
            for j in range(len(candidate)):
                if list(candidate[j]) in orders[i]:
                    frequent[j] += 1
        
        
        # delete not frequent frequentitem

    
    return answer

A = solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4])
=======
from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for k in course:
        candidates = []
        for menu_li in orders:
            for li in combinations(menu_li, k):
                res = ''.join(sorted(li))
                candidates.append(res)
        sorted_candidates = Counter(candidates).most_common()
        answer += [menu for menu, cnt in sorted_candidates if cnt > 1 and cnt == sorted_candidates[0][1]]
    return sorted(answer)
>>>>>>> 08e96cd0cc8891b5436724495b0bdadca612c0eb
