def solution(participant, completion):
    # 참가자와 완주자를 알파벳 순으로 sort를 한다.
    participant.sort()
    completion.sort()
    # 완주자를 기준으로 비교를 하였을 때, 같은 위치에 다른 사람의 이름이 있는 경우, 완주하지 못한 참가자이므로 이를 return 한다.
    for i in range(len(completion)):
        if completion[i] != participant[i]:
            return participant[i]
    # 만약 completion을 전부 돌았을 때까지 전부 같다면, 참가자의 리스트에서 마지막 남은 선수가 완주하지 못한 선수 이므로 이를 return 한다.
    return participant[-1]
