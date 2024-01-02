def solution(n, words):
    
    last_word = words[0]
    word_list = [last_word]
    person_num = 1
    round_num = 1
    
    for word in words[1:]:
        person_num += 1
        
        if last_word[-1] == word[0] and word not in word_list:
            last_word = word
            word_list.append(word)
            if person_num % n == 0:
                person_num = 0
                round_num += 1
        else:
            return [person_num, round_num]

    return [0, 0]