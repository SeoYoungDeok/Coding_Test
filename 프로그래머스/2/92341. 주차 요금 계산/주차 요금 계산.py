from math import ceil
from collections import defaultdict

def solution(fees, records):
    answer = []
    
    parking = dict()
    minute = defaultdict(int)
    
    for record in records:
        time, number, in_out = record.split()
        
        if in_out == 'IN':
            parking[number] = time
        else:
            in_time = parking[number]
            m = (int(time.split(':')[0]) - int(in_time.split(':')[0])) * 60 + (int(time.split(':')[1]) - int(in_time.split(':')[1]))
            minute[number] += m
            parking[number] = 0
    
    for k, v in parking.items():
        if v != 0:
            in_time = parking[k]
            m = (23 - int(in_time.split(':')[0])) * 60 + (59 - int(in_time.split(':')[1]))
            minute[k] += m
    
    for k, v in minute.items():
        if v <= fees[0]:
            minute[k] = fees[1]
        else:
            minute[k] = fees[1] + ceil((v - fees[0]) / fees[2]) * fees[3]
            
    for k, v in sorted(minute.items(), key = lambda x: x[0]):
        answer.append(v)
    
    return answer