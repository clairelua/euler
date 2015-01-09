import math


def isprime(x):
    end = int(math.sqrt(x))
    for y in xrange(2, end):
        if x % y == 0:
            return False
    return True

num = 600851475143
start = int(math.sqrt(num))
for x in xrange(start, 1, -1):
    if num % x == 0:
        print x
        if isprime(x):
            print "prime", x
            breaks
