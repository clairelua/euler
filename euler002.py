y = 0
a = 0
b = 1
c = a + b
while (c < 4000000):
    c = a + b
    a = b
    b = c

    if c % 2 == 0:
        y = y + c

print y
