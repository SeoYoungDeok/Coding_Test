def solution(skill, skill_trees):
    answer = 0
    
    for skills in skill_trees:
        idx = 0
        flag = 1
        for s in skills:
            if s in skill:
                if skill.find(s) == idx:
                    idx += 1
                else:
                    flag = 0
                    break
        if flag:
            answer += 1
        
    return answer