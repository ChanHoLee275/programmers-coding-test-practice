def calcMatrixElement(arr1, arr2, i, j, length):
    element = 0
    for k in range(length):
        element += arr1[i][k] * arr2[k][j]
    return element

def solution(arr1, arr2):
    answer = [[0]*len(arr2[0]) for i in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            answer[i][j] = calcMatrixElement(arr1, arr2, i, j, len(arr2))
    return answer