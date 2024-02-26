import sys
queue = []
front = -1
back = -1
cnt = int(sys.stdin.readline())
for i in range(cnt):
    op = sys.stdin.readline().split()
    if op[0] == "push":
        back += 1
        queue.append(op[1])
        continue
    if (op[0] == "front"):
        if (front == back):
            print(-1)
        else:
            print(queue[front + 1])
        continue
    if (op[0] == "back"):
        if (front == back):
            print(-1)
        else:
            print(queue[back])
        continue
    if (op[0] == "size"):
        print(back - front)
        continue
    if (op[0] == "empty"):
        if (front == back):
            print(1)
        else:
            print(0)
        continue
    if (op[0] == "pop"):
        if (front == back):
            print(-1)
        else:    
            front += 1
            print(queue[front])
        continue