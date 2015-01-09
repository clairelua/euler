mult = []

for y in range(100, 1000):
    for x in range(100, 1000):
        z = y * x
        t = str(z)
        reverset = t[::-1]
        if reverset == t:
            mult.append(z)

mult.sort()
print mult[-1]
