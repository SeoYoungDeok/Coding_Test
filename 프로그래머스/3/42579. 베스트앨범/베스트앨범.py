from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    best_album = defaultdict(list)
    total_play = defaultdict(int)
    
    for i, (genre, play) in enumerate(zip(genres, plays)):
        best_album[genre].append((i, play))
        total_play[genre] += play
    
    for k, v in best_album.items():
        best_album[k] = sorted(v, key=lambda x : x[-1], reverse=True)
        
    total_play = sorted(total_play.items(), key=lambda x: x[-1], reverse=True)
    
    for k, _ in total_play:
        answer.extend([k for k, v in best_album[k][:2]])
        
    return answer