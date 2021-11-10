import math

def calc(number):
    location = math.log2(number)
    low = math.trunc(location)
    return number - 2**low

def solution(n):
    ans = 1
    location = 1
    n = calc(n)
    while n > 1:
        n = calc(n)
        ans += 1
    if n == 1:
        ans += 1
    return ans