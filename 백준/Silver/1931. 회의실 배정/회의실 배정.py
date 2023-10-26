n = int(input())

meeting_list = list()
count = 0

for _ in range(n):
    start, end = map(int, input().split())
    meeting_list.append([start, end])

meeting_list.sort(key=lambda x: (x[1], x[0]))

end = 0

for meet in meeting_list:
    if end <= meet[0]:
        count += 1
        end = meet[1]

print(count)