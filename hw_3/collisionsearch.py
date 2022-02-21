from hard import HashMatrix

hashes = {}
for a in range(0, 3):
    for b in range(0, 3):
        for c in range(0, 3):
            for d in range(0, 3):
                A = HashMatrix([[a, b], [c, d]])
                hashes[A] = hash(A)

for i in hashes.keys():
    for j in hashes.keys():
        if hashes[i] == hashes[j]:
            print(i, ',', j)
