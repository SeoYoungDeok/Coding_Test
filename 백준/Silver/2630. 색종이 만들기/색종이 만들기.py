from sys import stdin as s

N = int(s.readline().rstrip())

paper = list()
for _ in range(N):
    paper.append(list(map(int, s.readline().rstrip().split())))


def division(array, n):
    global blue, white

    if n >= 0:
        s = 0
        for row in array:
            s += sum(row)

        if s == n * n:
            blue += 1
            return
        elif s == 0:
            white += 1
            return
        else:
            slice1 = list()
            slice2 = list()
            slice3 = list()
            slice4 = list()

            for i in range(n):
                if i < n // 2:
                    slice1.append(array[i][: n // 2])
                    slice2.append(array[i][n // 2 :])
                else:
                    slice3.append(array[i][: n // 2])
                    slice4.append(array[i][n // 2 :])

            division(slice1, n // 2)
            division(slice2, n // 2)
            division(slice3, n // 2)
            division(slice4, n // 2)
    else:
        return


blue = 0
white = 0
division(paper, N)

print(white)
print(blue)
