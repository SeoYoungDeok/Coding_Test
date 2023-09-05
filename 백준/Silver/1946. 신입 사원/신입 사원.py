from sys import stdin as s

T = int(s.readline().strip())

for i in range(T):
    N = int(s.readline().strip())

    resume_score = []
    interview_score = []
    count = 1
    for j in range(N):
        resume, interview = map(int, list(s.readline().strip().split()))
        resume_score.append(resume)
        interview_score.append(interview)

    idx = sorted(range(len(resume_score)), key=lambda k: resume_score[k])
    hash = set(interview_score)
    minimum = interview_score[idx[0]]
    for k in idx[1:]:
        if minimum > interview_score[k]:
            count += 1
            minimum = interview_score[k]

    print(count)
