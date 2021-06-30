def split_string(p):
    if p == "":
        return ("","")
    left = 0
    right = 0
    index = list()
    for i in range(len(p)):
        if p[i] == "(":
            left += 1
        elif p[i] == ")":
            right += 1
        if left == right:
            index.append(i)
            break
    u_index = index.pop()
    u = p[0:u_index+1]
    v = p[u_index+1:]
    return (u,v)
        

def check_right(p):
    stack = list()
    for i in range(len(p)):
        if p[i] == "(":
            stack.append(p[i])
        else :
            if len(stack) == 0:
                return False
            stack.pop()
    return True

def convert_right(p,answer):
    (u,v) = split_string(p)

    if u == "":
        return u
    
    if check_right(u):
        answer += u
        answer += convert_right(v,"")
        return answer
    
    else :
        
        answer += "("
        answer += convert_right(v,"")
        answer += ")"
        u = list(u)
        del u[0]
        del u[-1]
        for i in range(len(u)):
            if u[i] == "(":
                answer += ")"
            elif u[i] == ")":
                answer += "("
        return answer

def solution(p):
    answer = convert_right(p,"")
    return answer
