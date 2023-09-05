from sys import stdin as s

rating_dict = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0,
}

total_grade = 0
total_rating = 0
for i in range(20):
    course, grade, rating = input().split()
    if rating == "P":
        continue
    else:
        total_grade += float(grade)
        total_rating += rating_dict[rating] * float(grade)

print(total_rating / total_grade)