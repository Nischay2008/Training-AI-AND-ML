import math 

num = 100
prime_sum = 0

while num <= 500:
    is_prime = True
    if num > 1:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_sum += num
    num += 1

print("Sum of prime numbers between 100 and 500 is:", prime_sum)
