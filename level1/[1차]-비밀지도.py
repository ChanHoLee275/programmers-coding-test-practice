def dec2bin(number,n):
    
    answer = ''
    
    while number // 2 != 0:
        answer += str(number%2)
        number = number // 2
    
    if number != 0:
        answer += str(number)
    
    while len(answer) != n:
        answer += "0"
        
    return answer[::-1]

def solution(n, arr1, arr2):
    answer = [[" "]*n for _ in range(n)]
    
    bin1 = list()
    bin2 = list()
    
    for i in range(len(arr1)):
        bin1.append(dec2bin(arr1[i],n))
        bin2.append(dec2bin(arr2[i],n))
    
    
    for i in range(len(bin1)):
        row1 = list(bin1[i])
        row2 = list(bin2[i])
        for j in range(len(row1)):
            if answer[i][j] == " " and (row1[j] == "1" or row2[j] == "1"):
                answer[i][j] = "#"
    
    for i in range(len(answer)):
        answer[i] = "".join(answer[i])
    
    return answer