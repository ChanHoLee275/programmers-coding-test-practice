def rotate(string):
    
    flag = True
    
    stack = list()
    
    for i in range(len(string)):
        new_item = string[i]
        if len(stack) != 0:
            past_item = stack.pop()
            if past_item == "[" and new_item == "]":
                pass
            elif past_item == "(" and new_item == ")":
                pass
            elif past_item == "{" and new_item == "}":
                pass
            else :
                stack.append(past_item)
                stack.append(new_item)
        elif len(stack) == 0:
            stack.append(new_item)
    
    if len(stack) != 0:
        flag = False
    
    item = string.pop(0)
    string.append(item)
    
    return flag

def solution(s):
    answer = 0
    s = list(s)
    for i in range(len(s)):
        if rotate(s):
            answer += 1
    return answer