import math

def convert_line(line):
    [date, end_time, duration] = line.split(' ')
    [hour, minute, second] = list(map(float, end_time.split(':')))
    end_time_second = 3600000*hour + 60000 * minute + second*1000
    duration = float(duration[0:-1])*1000 - 1000
    start_time_second = end_time_second - duration
    return [int(start_time_second) - 1000, int(end_time_second) + 999]

def solution(lines):
    queue = sorted(list(map(lambda x: convert_line(x), lines)), key=lambda x: x[0])
    hashTable = dict()
    for i in queue:
        [start, end] = i
        for j in range(start, end):
            key = (j, j + 1)
            if hashTable.get(key, False) == False:
                hashTable[key] = 1
            else:
                hashTable[key] += 1
    if list(hashTable.keys()) == []:
        answer = 1
    else:
        answer = max(hashTable.values())
    return answer
