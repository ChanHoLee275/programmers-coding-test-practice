def solution(board, moves):
    answer = 0
    # moves는 matrix에서 column을 선택하는 것
    # moves를 통해 column이 선택되면, 가장 위에 있는 요소를 뽑아서 옮김.
    # 2차원의 배열에 접근하는 것 보다 hash table을 활용하여 접근하는 것이 시간이 덜 걸릴 것이라고 판단.
    
    # dictionary 만들기
    
    board_dic = dict()
    
    for i in range(len(board)):
        board_dic[i+1] = list()
    
    # dictionary의 value를 list로 하여 업데이트
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != 0:
                board_dic[j+1].append(board[i][j])
    
    # 가장 아래에 있는 것이 가장 list의 최신 element에 위치하여 이를 바꿈
    
    for i in board_dic.keys():
        board_dic[i].reverse()
    
    # moves에 따라서 pop을 통해 element를 뽑아서 옮김.
    
    basket = list()
    
    for i in moves:
        
        if len(board_dic[i]) != 0:
        
            chosen = board_dic[i].pop()
            
            if len(basket) != 0:
                
                recentElement = basket.pop()
                
                if recentElement == chosen:
                    
                    answer += 2
                else:
                    
                    basket += [recentElement,chosen]
            else :
                basket.append(chosen)
        
        else :
            pass
        
        
    # 기존의 옮긴 list에서 pop을 통해 뽑았을 때, 같으면 사라짐, 아니면 2개를 넣음
    
    return answer
