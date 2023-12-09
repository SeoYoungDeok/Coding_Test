def solution(str1, str2):
    answer = 0
    
    str1 = str1.lower()
    str2 = str2.lower()
    
    str1 = [a + b for a, b in zip(str1[:-1], str1[1:]) if a.isalpha() and b.isalpha()]
    str2 = [a + b for a, b in zip(str2[:-1], str2[1:]) if a.isalpha() and b.isalpha()]

    a = str1.copy()
    union = str1.copy()

    for i in str2:
        if i not in a:
            union.append(i)
        else:
            a.remove(i)

    common = list()

    for i in str2:
        if i in str1:
            common.append(i)
            str1.remove(i)

    if len(common) == len(union):
        return(65536)
    else:
        return(int(len(common) / len(union) * 65536))