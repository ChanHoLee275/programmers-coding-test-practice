def solution(s):
    queue = []
    for i in list(s):
        if i == "(":
            queue.append(i)
        else :
            if len(queue) == 0 or queue.pop() != "(":
                return False
    if len(queue) != 0:
        return False
    return True