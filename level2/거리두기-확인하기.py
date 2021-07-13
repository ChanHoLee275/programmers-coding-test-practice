def partial(room,i,j):

    # 맨해튼 거리는 한 점으로부터 같은 거리에 있는 점들이 다이아몬드를 이룬다는 것을 응용하여 풀이
    
    if j+1 < 5 and room[i][j+1] == 'P':
        return 0
    elif i + 1 < 5 and room[i+1][j] == 'P':
        return 0
    elif i - 1 >= 0 and room[i-1][j] == 'P':
        return 0
    elif j - 1 >= 0 and room[i][j-1] == 'P':
        return 0
    elif (i+1 < 5 and j-1 >=0 and j + 1 < 5) and room[i+1][j] == 'O' and (room[i+1][j-1] == 'P' or room[i+1][j+1] == 'P'):
        return 0
    elif (i - 1 >= 0 and j - 1 >= 0 and j+1 < 5) and room[i-1][j] == 'O' and (room[i-1][j-1] == 'P' or room[i-1][j+1] == 'P'):
        return 0
    elif (i + 1 < 5 and i - 1 >= 0 and j + 1 < 5) and room[i][j+1] == 'O' and (room[i-1][j+1] == 'P' or room[i+1][j+1] == 'P'):
        return 0
    elif (i + 1 < 5 and i - 1 >= 0 and j - 1 >= 0) and room[i][j-1] == 'O' and (room[i+1][j-1] == 'P' or room[i-1][j-1] == 'P'):
        return 0
    elif i + 2 < 5 and room[i+1][j] == 'O' and room[i+2][j] == 'P':
        return 0
    elif j + 2 < 5 and room[i][j+1] == 'O' and room[i][j+2] == 'P':
        return 0
    elif i -2 >= 0 and room[i-1][j] == 'O' and room[i-2][j] == 'P':
        return 0
    elif j - 2 >= 0 and room[i][j-1] == 'O' and room[i][j-2] == 'P':
        return 0

    return 1
    
def check(room):
    answer = 1
    for i in range(5):
        for j in range(5):
            if room[i][j] == 'P':
                answer = partial(room,i,j)
                if answer == 0:
                    return answer
    return answer

def solution(places):
    answer = []
    for i in range(5):
        room = places.pop()
        answer.append(check(room))
    return answer[::-1]