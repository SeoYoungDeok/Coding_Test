import re

def solution(files):
    answer = []
    
    temp = list()
    for name in files:
        temp.extend(re.findall('([a-zA-Z\-\.\ ]+)([0-9]{0,5})(.*)', name))
    
    answer = sorted(temp, key=lambda x:(x[0].lower(), int(x[1])))
    answer = [''.join(file) for file in answer]
    return answer