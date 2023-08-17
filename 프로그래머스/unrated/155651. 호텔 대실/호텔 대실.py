def solution(book_time):
    answer = [0] * 1450
    
    for start, end in book_time:
        start_idx = (int(start.split(":")[0]) * 60) + int(start.split(":")[1])
        end_idx = (int(end.split(":")[0]) * 60) + int(end.split(":")[1])
        for i in range(start_idx, end_idx+10):
            answer[i] += 1
        
    return max(answer)