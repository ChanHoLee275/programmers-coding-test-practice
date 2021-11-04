import collections

def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    people = collections.deque(people)
    while len(people) > 1:
        maximum = people.popleft()
        minimum = people.pop()
        if maximum + minimum <= limit:
            answer += 1
        else :
            people.append(minimum)
            answer += 1
    if len(people) == 1:
        answer += 1
    return answer