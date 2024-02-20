n, k = map(int, input().split())

coin_list = list()
count = 0

for i in range(n):
    coin_list.append(int(input()))
    
coin_list.reverse()

for coin in coin_list:
    count += k // coin
    k %= coin
    if k == 0:
        break
print(count)