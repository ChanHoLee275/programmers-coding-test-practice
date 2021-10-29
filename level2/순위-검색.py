# 효율성이 없는 풀이
def solution(info, query):
    answer = [0]*len(query)
    info = list(map(lambda x: x.split(" "), info))
    query = list(map(lambda x: list(filter(lambda y: y != "-" and y != "and", x.split(" "))), query))
    for i in info:
        for j in range(len(query)):
            score = int(i.pop())
            limit = int(query[j].pop())
            if score >= limit:
                if len(query[j]) == 0:
                    answer[j] += 1
                elif set(i).issuperset(set(query[j])):
                    answer[j] += 1
            i.append(score)
            query[j].append(limit)
    return answer