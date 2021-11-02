# 완전 탐색
def square(x, y, matrix, length):
    length -= 1
    if x + length - 1 >= len(matrix) or y + length - 1 >= len(matrix[0]):
        return False
    for i in range(x, x + length):
        for j in range(y, y + length):
            if matrix[i][j] == 0:
                return False
    return True

def solution(board):
    answer = [0]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                length = 1
                while square(i, j, board, length + 1):
                    length += 1
                answer.append((length-1)**2)
    if len(answer) != 0:
        return max(answer)
    else:
        return 0

# DFS
def solution(board):
    answer = 0
    row = len(board)
    colum=len(board[0])
    for i in range(row):
        for j in range(colum):
            if i==0 or j==0:
                continue
            if board[i][j]!=0:
                board[i][j]=min(board[i-1][j-1],min(board[i-1][j],board[i][j-1]))+1
    li=[]
    for i in range(row):
        li.append(max(board[i]))
    return max(li)**2