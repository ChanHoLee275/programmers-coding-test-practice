def solution(n):
    answer = 0
    for i in range(1, n+1):
        acc = 0
        start = i
        while acc < n:
            acc += start
            start += 1
        if acc == n:
            answer += 1
    return answer