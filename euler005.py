power = {}

for x in range(2, 21):
    n = 2
    while x > 1:
        k = 0
        while x % n == 0:
            x = x / n
            k = k + 1
        if k > 0:
            if n not in power or power[n] < k:
                power[n] = k
        n = n + 1
print power

result = 1
for key, value in power.iteritems():
    result *= pow(key, value)

print result
