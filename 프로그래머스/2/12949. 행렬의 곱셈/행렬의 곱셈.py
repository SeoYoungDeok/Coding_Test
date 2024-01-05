def solution(arr1, arr2):
    answer = []
    
    I = len(arr1)
    J = len(arr1[0])
    K = len(arr2[0])
    
    for i in range(I):
        temp = list()
        for k in range(K):
            s = 0
            for j in range(J):
                s += arr1[i][j] * arr2[j][k]
            temp.append(s)
        answer.append(temp)
            
    return answer