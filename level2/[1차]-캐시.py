cache_hit = 1
cache_miss = 5

def solution(cacheSize, cities):
    answer = 0
    if cacheSize == 0:
        return len(cities)*cache_miss
        
    cache = [[" " for _ in range(cacheSize)],[0 for _ in range(cacheSize)]]
    
    time = 1
    
    for i in range(len(cities)):
        if cities[i].upper() in cache[0]:
            cache[1][cache[0].index(cities[i].upper())] = time
            answer += cache_hit
        else :
            index = cache[1].index(min(cache[1]))
            cache[0][index] = cities[i].upper()
            cache[1][index] = time
            answer += cache_miss
        time += 1
    
    return answer