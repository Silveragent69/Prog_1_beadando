list = []
db = 0
while True:
    str = input()
    if str == "end":
        break
    list.append(str)
mgh = "aeiouAEIOU"
for i in list:
    for j in i:
        if j in mgh:
            db += 1
avg = db / len(list)
print("Átlagos magánhangzószám: ", avg, "\nSzavak:")

for i in list:
    db = 0
    for j in i:
        if j in mgh:
            db += 1
    if avg < db:
        print(i, end=" ")
