def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # check up to sqrt(n)
        if n % i == 0:
            return False
    return True

def is_palindrome(n):
    return str(n) == str(n)[::-1]

prime_palindromes = []

for num in range(100, 501):
    if is_prime(num) and is_palindrome(num):
        prime_palindromes.append(num)

print("Prime Palindrome numbers between 100 and 500 are:")
print(prime_palindromes)
