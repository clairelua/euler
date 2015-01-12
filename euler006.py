num = 100

sum_of_sq = 0
for i in range(1, num + 1):
    sum_of_sq += i ** 2

sq_of_sum = sum(range(1, num + 1)) ** 2

print abs(sum_of_sq - sq_of_sum)
