def solution(cards1, cards2, goal):
    cards1 = cards1[::-1]
    cards2 = cards2[::-1]
    
    for word in goal:
        if len(cards1) > 0 and cards1[-1] == word:
            cards1.pop()
        elif len(cards2) > 0 and cards2[-1] == word:
            cards2.pop()
        else:
            return "No"
    
    return "Yes"