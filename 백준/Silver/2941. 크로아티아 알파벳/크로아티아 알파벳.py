from sys import stdin as s

word = s.readline().strip()

croatia_alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for alphabet in croatia_alphabet:
    word = word.replace(alphabet, "0")

print(len(word))
