def solution(players, callings):
    ranking = {name:i for i, name in enumerate(players)}
    
    for call in callings:
        current_rank = ranking[call]
        
        ranking[call] -= 1
        ranking[players[current_rank-1]] += 1
        
        temp = players[current_rank]
        players[current_rank] = players[current_rank-1]
        players[current_rank-1] = temp
    
    return players