from collections import deque

def solution(priorities, location):
    printer = deque(priorities)
    if len(printer) == 1:
        return 1
    
    answer = 0
    while True:
        if printer[0] < max(printer):
            printer.rotate(-1)
            location -= 1
            if location == -1:
                location = len(printer) - 1
        else:
            if location == 0:
                return answer + 1
            else:
                printer.popleft()
                answer += 1
                location -= 1
                if location == -1:
                    location = len(printer) - 1