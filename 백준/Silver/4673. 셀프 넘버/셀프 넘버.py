import sys

not_self_num = set()

def d(n):
    str_num = str(n)
    s = 0
    for c in str_num:
        s += int(c)
    next_num = n + s
    not_self_num.add(next_num)
    if next_num <= 10000:
        d(next_num)
    else:
        return


for i in range(1, 10000):
    d(i)
    

not_self_num_list = list(not_self_num)
not_self_num_list.sort()

for i in range(1, 10000):
    if i not in(not_self_num_list):
        print(i)