def JaccardCoefficient(A,B):
    if len(A) == len(B) == 0:
        return 1
    intersection = 0
    length = len(B)
    for i in range(len(A)):
        if A[i] in B:
            B.remove(A[i])
            intersection += 1
    return intersection / (len(A) + length - intersection)
        

def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    string1 = list()
    string2 = list()
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
            string1.append(str1[i:i+2])
    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha():
            string2.append(str2[i:i+2])
    answer = JaccardCoefficient(string1,string2)
    answer *= 65536
    return int(answer)