import heapq
from collections import deque

def solution(jobs):
    
    answer = 0
    time = 0
    working_time = 0
    jobs = sorted(jobs, key=lambda x : x[0])
    jobs = deque(jobs)
    jobs_cnt = len(jobs)
    queue = list()
    
    while True:
        while jobs and jobs[0][0] == time:
            pop = jobs.popleft()
            heapq.heappush(queue, [pop[1], pop[0]])
        
        if queue and working_time <= 0:
            working_time, request_time = heapq.heappop(queue)
        
        working_time -= 1
        time += 1
        
        if working_time == 0:
            answer += time - request_time
        
        if not jobs and not queue and working_time <= 0:
            break
            
    return answer // jobs_cnt