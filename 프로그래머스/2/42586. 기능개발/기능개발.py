from math import ceil
def solution(progresses, speeds):
    answer = []
    work_duration = list()
    for i in range(len(progresses)):
        work_duration.append(ceil((100-progresses[i]) / speeds[i]))
        
    cnt = 1
    max_work = work_duration[0]
    for i in range(1, len(work_duration)):
        if max_work >= work_duration[i]:
            cnt += 1
        elif max_work < work_duration[i]:
            answer.append(cnt)
            cnt = 1
            max_work = work_duration[i]
    answer.append(cnt)
    return answer