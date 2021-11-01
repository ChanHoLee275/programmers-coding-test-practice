def sortByInt(array):
    answer = []
    table = dict()
    for i in array:
        number = []
        flag = 0
        for j in list(i):
            if flag == 0 and j.isnumeric():
                number.append(j)
            elif len(number) != 0:
                flag = 1
        if int(''.join(number)) in table.keys():
            table[int(''.join(number))].append(i)
        else:
            table[int(''.join(number))] = [i]
    keys = list(table.keys())
    keys.sort()
    for i in keys:
        answer += table[i]
    return answer
                              
def solution(files):
    answer = []
    table = dict()
    for i in files:
        number = []
        flag = 0
        for j in list(i):
            if flag == 0 and not j.isnumeric():
                number.append(j.upper())
            elif len(number) != 0:
                flag = 1
        if ''.join(number) in table.keys():
            table[''.join(number)].append(i)
        else:
            table[''.join(number)] = [i]
    keys = list(table.keys())
    keys.sort()
    
    for i in keys:
        answer += sortByInt(table[i])
    return answer