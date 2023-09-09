from sys import stdin as s

K = int(s.readline().strip())

array = s.readline().strip().split()
visited = [False] * 10


def check(num1, num2, sign):
    if sign == ">":
        return num1 > num2
    else:
        return num1 < num2


def go(k, num):
    global minimum, maximum
    if k == K + 1:
        if len(minimum) == 0:
            minimum = num
        else:
            maximum = num
        return

    for i in range(10):
        if not visited[i]:
            if k == 0 or check(num[-1], str(i), array[k - 1]):
                visited[i] = True
                go(k + 1, num + str(i))
                visited[i] = False


minimum = ""
maximum = ""
go(0, "")

print(maximum)
print(minimum)
