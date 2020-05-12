import string
szo = input("Adjon meg egy stringet: ")
d = dict.fromkeys(string.ascii_uppercase, 0)
str2 = ""
db = 1
j = szo[0]
i = ""
for i in szo:
    if i == j:
        d[i] += 1
        db = d[i]
    else:
        str2 += str(db) + j
        d[i] = 1
        db = 1
    j = i
if i == j:
    str2 += str(db) + j
print(str2)
