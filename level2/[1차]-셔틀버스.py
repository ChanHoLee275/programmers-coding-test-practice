def solution(n, t, m, timetable):
    answer = ''
    timetable_dict = dict()
    minute = 0
    hour = 9
    
    # dictionary key 생성
    for i in range(n):
        if minute // 60 == 1:
            minute -= 60
            hour += 1
        timetable_dict[(hour,minute)] = []
        minute += t
    
    
    keys = timetable_dict.keys()
    keys = list(keys)
    
    # timetable dictionary에 입력
    
    for i in range(len(timetable)):
        timetable[i] = timetable[i].split(":")
        timetable[i][0] = int(timetable[i][0])
        timetable[i][1] = int(timetable[i][1])

        for j in keys:
            (hour,minute) = j
            if timetable[i][0] < hour and len(timetable_dict[j]) < m:
                timetable_dict[j].append(timetable[i])
                break
            elif timetable[i][0] == hour and timetable[i][1] <= minute and len(timetable_dict[j]) < m:
                timetable_dict[j].append(timetable[i])
                break
    
    i = keys.pop()
    
    candidate = timetable_dict[i]
    
    if len(candidate) >= m:
        for i in range(len(candidate)):
            candidate[i] = candidate[i][0]*60 + candidate[i][1]
        candidate.sort()
        time = candidate[m-1]
        time -= 1
        if time == -1:
            time = 0
        hour = time // 60
        minute = time % 60
        hour = str(hour)
        minute = str(minute)
        if len(hour) == 1:
            hour = "0" + hour
        if len(minute) == 1:
            minute = "0" + minute
        return hour + ":" + minute
    else :
        hour = i[0]
        minute = i[1]
        hour = str(hour)
        minute = str(minute)
        if len(hour) == 1:
            hour = "0" + hour
        if len(minute) == 1:
            minute = "0" + minute
        return hour + ":" + minute
            
    return answer