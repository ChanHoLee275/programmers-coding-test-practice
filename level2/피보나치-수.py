def solution(n):
    if n == 2:
        return 1
    fiboArray = [0, 1, 1]
    for i in range(n-2):
        fiboArray.append((fiboArray[-1] + fiboArray[-2]) % 1234567)
    return fiboArray[-1]