def solution(n, left, right):
    answer = []
    row_left = left // n
    row_right = right // n
    column_left = left % n
    column_right = right % n
    
    if row_left == row_right:
        for i in range(column_left, column_right + 1):
            if i >= row_left:
                answer.append(i+1)
            else:
                answer.append(row_left + 1)
        return answer
    
    for i in range(column_left, n):
        if i >= row_left:
            answer.append(i + 1)
        else:
            answer.append(row_left + 1)
    for i in range(row_left + 1, row_right):
        for j in range(n):
            if i >= j:
                answer.append(i + 1)
            else:
                answer.append(j + 1)
    for i in range(0, column_right + 1):
        if i >= row_right:
            answer.append(i + 1)
        else:
            answer.append(row_right + 1)
    return answer