def solution(s):
    answer = ''
    flag = 1
    for c in s:
        if c.isalpha() and flag:
            answer += c.upper()
            flag = 0
        elif c.isdigit() and flag:
            answer += c
            flag = 0
        elif c == " ":
            answer += " "
            flag = 1
        elif not flag:
            answer += c.lower()
    return answer