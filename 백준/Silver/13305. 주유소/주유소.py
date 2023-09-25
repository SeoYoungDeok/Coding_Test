city = int(input())
distances = list(map(int, input().split()))
costs = list(map(int, input().split()))

temp_cost = costs[0]
answer = 0

for i in range(city - 1):
    if costs[i] <= temp_cost:
        temp_cost = costs[i]
    
    answer += temp_cost * distances[i]
    
print(answer)