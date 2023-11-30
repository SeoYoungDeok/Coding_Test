def solution(record):
    answer = []
    
    name_dict = dict()
    for data in record:
        if data.split()[0] == 'Change' or data.split()[0] == 'Enter':
            name_dict[data.split()[1]] = data.split()[2] 
    
    for data in record:
        if data.split()[0] == 'Enter':
            answer.append(name_dict[data.split()[1]] + "님이 들어왔습니다.")
        elif data.split()[0] == 'Leave':
            answer.append(name_dict[data.split()[1]] + "님이 나갔습니다.")
        
    return answer