def solution(msg):
    answer = []
    table = dict()
    for i in range(26):
        table[chr(i + 65)] = i + 1
    past_index = 0
    next_index = 1
    number = 26
    while next_index < len(msg):
        if msg[past_index:next_index] in table.keys() and not msg[past_index:next_index+1] in table.keys():
            answer.append(table[msg[past_index:next_index]])
            number += 1
            table[msg[past_index:next_index+1]] = number
            past_index = next_index
            next_index = past_index + 1
        else :
            next_index += 1
    answer.append(table[msg[past_index:next_index]])
    return answer