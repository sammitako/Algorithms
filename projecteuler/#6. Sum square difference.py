# The sum of the squares of the first ten natural numbers is,
# 1**2 + 2**2 + ... + 10**2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)**2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
# 3025 - 385 = 2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sqfirst(a, b):
    result = 0
    for i in range(a, b):
        result += i*i
    return result

def plsfirst(a, b):
    result = 0
    for i in range(a, b):
        result += i
    result = result*result
    return result

print(plsfirst(1, 101) - sqfirst(1, 101)) # 25164150