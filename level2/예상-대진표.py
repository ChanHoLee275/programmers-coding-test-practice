def solution(n,a,b):
    # 대진표를 프로그래밍으로 만든 것
    answer = 1
    
    participate = list(range(n))
    
    participate[a-1] = "A"
    participate[b-1] = "B"
    
    while participate:

        index = list()
        
        for i in range(0,len(participate),2):

            if "A" in participate[i:i+2] and "B" in participate[i:i+2]:
                
                return answer
            
            elif "A" in participate[i:i+2] and not("B" in participate[i:i+2]):
                
                if participate[i] == "A":
                    
                    index.append(participate[i+1])
                    
                else :
                    
                    index.append(participate[i])
                    
            elif not("A" in participate[i:i+2]) and "B" in participate[i:i+2]:
                
                if participate[i] == "B":
                    
                    index.append(participate[i+1])
                    
                else :
                    
                    index.append(participate[i])
            else :
                
                index.append(participate[i])
            
        for i in index:
            
            participate.remove(i)
            
        answer += 1
        
    return answer

def solution(n,a,b):
    
    # 인덱스만을 활용해서 계산
    answer = 1
    a -= 1
    b -= 1
    while True:
        if a //2 == b//2:
            break
        else :
            a = a//2
            b = b//2
        answer += 1
    return answer