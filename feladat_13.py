import numpy as np


def agrajz(n):
    global db
    global masolat
    global bajnoksag
    szotar = {}
    csapat = []
    golok = []
    tovabb = []
    for i in range(1, n + 1):
        gol = np.random.randint(1, 9, size=1)
        szotar['Team' + str(i)] = gol
    for k, v in szotar.items():
        csapat.append(k)
        golok.append(v)
    if len(masolat) != 0:
        csapat = masolat
    i = 0
    while i < n - 1:
        if golok[i] > golok[i + 1]:
            tovabb.append(csapat[i])
        else:
            tovabb.append(csapat[i + 1])
        i += 2
    masolat = tovabb
    bajnoksag.append(tovabb)
    db = len(tovabb)


temp = []
bajnoksag = []
masolat = []
kozteskihagyas = []
aktualiskihagyas = [0]
my_file = open("Sportesemeny.txt", "w")

while True:
    n = int(input("Adja meg a csapatok számát: "))
    n2 = n
    if n2 % 2 == 0:
        while n2 > 2:
            n2 = n2 / 2
        if n2 == 2:
            break
db = n

for i in range(1, n + 1):
    temp.append('Team' + str(i))

bajnoksag.append(temp)
korok = 0

while db > 1:
    agrajz(db)
    korok += 1

for j in range(korok):
    if j == 0:
        kozteskihagyas.append(1)
    else:
        kozteskihagyas.append(kozteskihagyas[j - 1] * 2 + 1)

aktualiskihagyas += kozteskihagyas
for s in range(n * 2 - 1):
    for o in range(korok + 1):
        if aktualiskihagyas[o] != 0:
            if o == 0:
                print("\t\t\t", end="", file=my_file)
            else:
                print("\t\t\t\t", end="", file=my_file)
            aktualiskihagyas[o] -= 1
        else:
            if len(bajnoksag[o]) != 0:
                if o != 0:
                    print("|--->", end="", file=my_file)
                print(bajnoksag[o].pop(0), end="", file=my_file)
                if o != len(kozteskihagyas):
                    print("---", end="", file=my_file)
                if o < len(kozteskihagyas) and len(bajnoksag[o]) > 0:
                    aktualiskihagyas[o] = kozteskihagyas[o]
    print(" ", file=my_file)
my_file.close()
