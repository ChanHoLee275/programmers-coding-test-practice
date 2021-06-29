import itertools
import copy

# 완전 탐색 문제

def solution(expression):
    
    calculateion = ["+","-","*"]
    pairs = itertools.permutations(calculateion,3)
    pairs = list(pairs)
    
    expression_list = list()
    counts = [0]*3
    number = ''
    for i in range(len(expression)):
        if expression[i].isnumeric():
            number += expression[i]
        else :
            expression_list.append(int(number))
            expression_list.append(expression[i])
            index = calculateion.index(expression[i])
            counts[index] += 1
            number = ''
    expression_list.append(int(number))
    numbers = []
    for i in range(len(pairs)):
        calculate = copy.deepcopy(expression_list)
        for j in list(pairs[i]):
            count = counts[calculateion.index(j)]
            for k in range(count):
                index = calculate.index(j)
                if j == "-":
                    num1 = calculate.pop(index-1)
                    cal = calculate.pop(index-1)
                    num2 = calculate.pop(index-1)
                    calculate.insert(index-1,num1-num2)
                elif j == "+":
                    num1 = calculate.pop(index-1)
                    cal = calculate.pop(index-1)
                    num2 = calculate.pop(index-1)
                    calculate.insert(index-1,num1+num2)
                else :
                    num1 = calculate.pop(index-1)
                    cal = calculate.pop(index-1)
                    num2 = calculate.pop(index-1)
                    calculate.insert(index-1,num1*num2)
        numbers.append(abs(calculate[0]))
    return max(numbers)