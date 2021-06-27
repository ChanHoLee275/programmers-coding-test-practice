def solution(s):
        
    # i is length
    numbers = list()
    for i in range(1,len(s)//2+2):
        string_list = list()
        for j in range(0,len(s),i):
            string_list.append(s[j:j+i])
        string_list = string_list[::-1]
        standard = string_list.pop()
        count = 1
        string = ''
        while len(string_list) != 0:
            candidate = string_list.pop()
            if standard == candidate:
                count +=1
            else :
                if count == 1:
                    string += standard
                    standard = candidate
                    count = 1
                else :
                    string += str(count)
                    string += standard
                    standard = candidate
                    count = 1
        if count == 1:
            string += standard
        else :
            string += str(count)
            string += standard
        numbers.append(len(string))
        
                
    return min(numbers)
print(solution("aabbaccc"))