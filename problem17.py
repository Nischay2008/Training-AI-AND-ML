import math

print("Strong numbers between 1 and 1000 using for loop:")

for num in range(1, 1001):  # loop through 1–1000
    temp = num
    sum_fact = 0

    # process each digit using while loop
    while temp > 0:
        digit = temp % 10
        sum_fact += math.factorial(digit)
        temp //= 10

    if sum_fact == num:
        print(num)
