def solution(name, yearning, photo):
    answer = []
    
    for a in photo:
        score = 0
        for person in a:
            try:
                score += yearning[name.index(person)]
            except ValueError:
                pass
        answer.append(score)
    
    return answer