import math

def solution(brown, yellow):
    total = brown + yellow

    x = int(math.sqrt(total))
    y = int(math.sqrt(total))

    if x * y == total:
        return [x, y]
    else:
        while 1:
            if x * y < total:
                x += 1
            elif x * y > total:
                if y <= 3:
                    x += 1
                else:
                    y -= 1
            elif x * y == total:
                if (x-2) * (y-2) == yellow:
                    break
                else:
                    y -= 1

        return [x, y]