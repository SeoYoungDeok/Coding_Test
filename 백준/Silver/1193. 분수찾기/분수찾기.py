n = int(input())

count = 1

while(True):
    if (n - count) > 0:
        n = n - count
        count += 1
    else:
        break

if (count % 2) != 0:
    if n == 0:
        answer = str(count - (n-1)) + '/1'
    else:
        answer = str(count - (n-1)) + '/' + str(n)
else:
    if n == 0:
        answer = '1/' + str(count - (n-1))
    else:
        answer = str(n) + '/' + str(count - (n-1))

print(answer)