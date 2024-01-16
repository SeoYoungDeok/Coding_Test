import re

def solution(m, musicinfos):
    answer_music = "(None)"
    answer_len = 0
    
    for music in musicinfos:
        start_time, end_time, title, melody = music.split(",")
        start_idx = (int(start_time.split(":")[0]) * 60) + int(start_time.split(":")[1])
        end_idx = (int(end_time.split(":")[0]) * 60) + int(end_time.split(":")[1])
        for k, v in {"C#": "c", "D#": "d", "F#": "f", "G#": "g", "A#": "a"}.items():
            melody = re.sub(k, v, melody)
            m = re.sub(k, v, m)
        repeat, remain = divmod((end_idx - start_idx), len(melody))
        full_melody = (melody * repeat) + melody[:remain]
        
        search = re.search(m, full_melody)
        if search and answer_len < len(full_melody):
            answer_music = title
            answer_len = len(full_melody)
    
    return answer_music