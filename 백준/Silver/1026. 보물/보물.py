n = int(input())

a = input().split()
a = list(map(int, a))
b = input().split()
b = list(map(int, b))

a.sort()
b.sort(reverse=True)

a_b_sum = 0
for i in range(n):
    a_b_sum += a[i] * b[i]
    
print(a_b_sum)