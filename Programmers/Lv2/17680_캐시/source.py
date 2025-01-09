from collections import deque

def solution(cacheSize, cities):
    buffer = deque(maxlen=cacheSize)
    total = 0
    
    if cacheSize == 0:
        return len(cities) * 5
    
    for city in cities:
        city = city.lower()
        
        if city in buffer:
            total += 1
            buffer.remove(city)
            buffer.append(city)
            
        else:
            total += 5
            buffer.append(city)
            
    return total