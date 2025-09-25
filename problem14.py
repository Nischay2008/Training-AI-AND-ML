# Take a prime number and write 
x = int(input("Enter the value X "))

prime = []

for i in range (1 , x + 1):
    if x % i == 0:
        prime.append(i)

if len(prime) == 2:
    print(f"{i} is a Prime number.")
else:
    print(f"{i} is not a prime number.")