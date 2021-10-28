import itertools
def transpose(lists):
    return [list(i) for i in zip(*lists)]

def IsKeys(check, keys):
    for i in keys:
        if set(check).issuperset(set(i)):
            return False
    return True
            

def solution(relation):
    answer = 0
    column = [i for i in range(len(relation[0]))]
    numbers = len(relation)
    candidate = []
    relation = transpose(relation)
    for i in range(1,len(relation[0])+1):
        candidate += list(itertools.combinations(column, i))
    keys = []
    for i in candidate:
        key = list(i)
        parts = []
        for j in key:
            parts.append(relation[int(j)])
        check = []
        for j in range(len(parts[0])):
            input_pair = []
            for k in range(len(parts)):
                input_pair.append(parts[k][j])
            check.append(tuple(input_pair))
        if len(set(check)) == numbers and IsKeys(key, keys):
            keys.append(key)
            answer += 1
    return answer
