# [1차] 캐시

## **📝문제 설명**
지도개발팀에서 근무하는 제이지는 지도에서 도시 이름을 검색하면 해당 도시와 관련된 맛집 게시물들을 데이터베이스에서 읽어 보여주는 서비스를 개발하고 있다.
이 프로그램의 테스팅 업무를 담당하고 있는 어피치는 서비스를 오픈하기 전 각 로직에 대한 성능 측정을 수행하였는데, 제이지가 작성한 부분 중 데이터베이스에서 게시물을 가져오는 부분의 실행시간이 너무 오래 걸린다는 것을 알게 되었다.
어피치는 제이지에게 해당 로직을 개선하라고 닦달하기 시작하였고, 제이지는 DB 캐시를 적용하여 성능 개선을 시도하고 있지만 캐시 크기를 얼마로 해야 효율적인지 몰라 난감한 상황이다.

어피치에게 시달리는 제이지를 도와, DB 캐시를 적용할 때 캐시 크기에 따른 실행시간 측정 프로그램을 작성하시오.
### **⚠제한사항**
- 캐시 교체 알고리즘은 LRU(Least Recently Used)를 사용한다.
- cache hit일 경우 실행시간은 1이다.
- cache miss일 경우 실행시간은 5이다.
### **입출력 예**
캐시크기(cacheSize) | 도시이름(cities) | 실행시간
----------------|--------------|-----
3 | ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"] | 50
3 | ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"] | 21
2 | ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"] | 60
5 | ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"] | 52
2 | ["Jeju", "Pangyo", "NewYork", "newyork"] | 16
0 | ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"] | 25
## **🧐CODE REVIEW**

### **😫나의 오답 풀이**

### **🧾나의 풀이**

```python
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
```

#### **📝해설**

```python
from collections import deque

def solution(cacheSize, cities):
    # deque를 버퍼로써 사용. 버퍼 최대크기에 도달한 경우 append시 자동으로 가장 오래된 자료 pop
    buffer = deque(maxlen=cacheSize)
    total = 0
    
    # cache가 0일경우 예외처리
    if cacheSize == 0:
        return len(cities) * 5
    
    # 도시들을 입력받으면서
    for city in cities:

        # 대소문자 구분 X
        city = city.lower()
        
        # 만약 캐시에 있는 도시라면
        if city in buffer:
            total += 1
            buffer.remove(city)
            buffer.append(city)
        
        # 캐시에 없는 도시라면
        else:
            total += 5
            buffer.append(city)
            
    return total
```

### **다른 풀이**

```python
# LRU cache reference : https://www.kunxi.org/blog/2014/05/lru-cache-in-python/
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.tm = 0
        self.cache = {}
        self.lru = {}

    def get(self, key):
        if key in self.cache:
            self.lru[key] = self.tm
            self.tm += 1
            return self.cache[key]
        return -1

    def set(self, key, value):
        if len(self.cache) >= self.capacity:
            # find the LRU entry
            old_key = min(self.lru.keys(), key=lambda k:self.lru[k])
            self.cache.pop(old_key)
            self.lru.pop(old_key)
        self.cache[key] = value
        self.lru[key] = self.tm
        self.tm += 1


def solution(cacheSize, cities):
    process_time = 0
    if cacheSize != 0:
        cache = LRUCache(cacheSize)
        for city in cities:
            if cache.get(city.lower()) == -1:
                cache.set(city.lower(), city)
                process_time += 5
            else:
                process_time += 1
    else:
        process_time = len(cities) * 5

    return process_time
```

## 📚참고 사이트

- **🔗[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/17680)**<br/>