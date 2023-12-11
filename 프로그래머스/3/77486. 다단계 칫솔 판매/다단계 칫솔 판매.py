import math

def solution(enroll, referral, seller, amount):
    referral_dict = {k:v for k, v in zip(enroll, referral)}
    answer = {k:0 for k in enroll}
    
    for k, v in zip(seller, amount):
        v *= 100
        answer[k] += v - math.trunc(v * 0.1)
        v = math.trunc(v * 0.1)
        
        while referral_dict[k] != "-":
            k = referral_dict[k]
            if v - math.trunc(v * 0.1) <= 1:
                answer[k] += v
                break
            else:
                answer[k] += v - math.trunc(v * 0.1)
            v = math.trunc(v * 0.1)
    answer = list(answer.values())
    return answer