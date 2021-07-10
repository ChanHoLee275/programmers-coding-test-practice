def solution(dartResult):

    array = list(dartResult)
    numbers = list()
    
    try :
        for i in range(len(array)):
            if array[i] == '1' and array[i+1] == '0':
                array[i] = '10'
                del array[i+1]
    except IndexError:
        print("Index Error but ignore.")
    
    for i in array:
        if i.isnumeric():
            numbers.append(int(i))
        elif i.isalpha():
            number = numbers.pop()
            if i == "S":
                numbers.append(number)
            elif i == "D":
                numbers.append(number**2)
            elif i == "T":
                numbers.append(number**3)
        else :
            numbers.append(i)
    
    answer = list()
    
    for i in range(len(numbers)):
        if numbers[i] != "*" and numbers[i] != "#":
            answer.append(numbers[i])
        elif numbers[i] == "*" :
            if i != 1:
                A = answer.pop()
                B = answer.pop()
                answer.append(B*2)
                answer.append(A*2)
            else :
                A = answer.pop()
                answer.append(A*2)
        elif numbers[i] == "#":
            A = answer.pop()
            answer.append(-A)
    return sum(answer)