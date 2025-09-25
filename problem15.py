import math 

num = 100
while num <= 500:
    is_prime = True
    if num > 1:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num > 1:
                for i in range(2, int(math.sqrt(num)) +1):
                    if num % i == 0:
                        is_prime = False
                        break
                    if is_prime:
                        print(num, end=", ")
                    num += 1

