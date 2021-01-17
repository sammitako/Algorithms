# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# 방법1
# lcm(a, b) = a * b / gcd(a, b)

from functools import reduce
def gcd(a, b):
    if a < b:
        (a, b) = (b, a)
    while b != 0:
        (a, b) = (b, a%b)
    return a

def lcm(a, b):
    return a * b / gcd(a, b)

result = reduce(lambda a, b: lcm(a, b), range(1, 21))
print(result)


# 방법2
import math

result = []
lcm = 1
for i in range(1, 21):
    gcd = math.gcd(i, lcm)
    lcm = int(i*lcm / gcd)
    result.append(lcm)
print(max(result)) # 232792560
