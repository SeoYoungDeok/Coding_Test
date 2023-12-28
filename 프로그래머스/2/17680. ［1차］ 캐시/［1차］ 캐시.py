def solution(cacheSize, cities):
    answer = 0
    cache = list()
    
    if cacheSize == 0:
        return len(cities) * 5
    
    for city in cities:
        city = city.lower()
        
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
        else:
            answer += 5
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                del cache[0]
                cache.append(city)
            
    return answer