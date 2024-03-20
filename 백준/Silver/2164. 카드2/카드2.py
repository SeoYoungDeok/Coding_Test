queue = []
front = -1
back = -1
N = int(input())
for i in range(1, N+1):
    back += 1
    queue.append(i)
i = 1
while True:
    if (i % 2 != 0):
        front += 1
    else:
        front += 1
        back += 1
        queue.append(queue[front])
    if (front == back):
        break
    i += 1

print(queue.pop())