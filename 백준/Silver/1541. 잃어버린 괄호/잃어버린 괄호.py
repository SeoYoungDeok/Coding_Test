exp = input()

idx = 0
for i, c in enumerate(exp):
    if c == '-':
        idx = i
        break
        
if idx == 0:
    print(sum(list(map(int, exp.replace('-', '+').split('+')))))
else:   
    left = exp[:idx]
    right = exp[idx+1:]

    left_list = list(map(int, left.replace('-', '+').split('+')))
    right_list = list(map(int, right.replace('-', '+').split('+')))

    left_sum = sum(left_list)
    right_sum = sum(right_list)

    print(left_sum - right_sum)