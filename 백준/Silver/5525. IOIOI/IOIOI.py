import sys

input = sys.stdin.readline

def make_table(pattern):
    p_len = len(pattern)
    table = [0 for _ in range(p_len)]
    
    pidx = 0
    for idx in range(1, p_len):
        while pidx > 0 and pattern[idx] != pattern[pidx]:
            pidx = table[pidx-1]
        
        if pattern[idx] == pattern[pidx]:
            pidx += 1
            table[idx] = pidx
    
    return table

def KMP(word, pattern):
    table = make_table(pattern)
    
    results = []
    pidx = 0
    
    for idx in range(len(word)):
        while pidx > 0 and word[idx] != pattern[pidx]:
            pidx = table[pidx-1]
        if word[idx] == pattern[pidx]:
            if pidx == len(pattern)-1:
                results.append(idx-len(pattern)+2)
                pidx = table[pidx]
            else:
                pidx += 1
    
    return len(results)

N = int(input())
M = int(input())
S = input().rstrip()
pattren = 'I' * (N+1)
pattren = 'O'.join(pattren)
print(KMP(S, pattren))