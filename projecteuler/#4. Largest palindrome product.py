# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

result = []
for i in range(900, 1000):
    for j in range(900, 1000):
        num = i*j
        if str(num) == str(num)[::-1]:
            result.append(num)
print(max(result)) # 906609
