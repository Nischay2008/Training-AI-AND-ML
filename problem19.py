import time

num = int(input("Enter a number: "))



for i in range(1 , 11):
    print(f"{num} x {i} = {num * i}")
    time.sleep(0.1)


print("")
print("This is with while loop")
time.sleep(2)


a = 1
while a <= 10:
    print(f"{num} x {a} = {num*a}")
    a += 1
    time.sleep(0.1)

print("")

count = 0
for k in range(1,6):
    count += k
print(f"The sum of first 5 natural numbers are = {count}")

print("")

# While loop
p = 0
l = 0
while p <= 5:
    
    l += p
    p += 1

print(f"the sum of first 5 natural numbers with while = {l}")


print("")

for o in range(5 , 0 ,-1):
    print(o)
    time.sleep(0.5)

print("")

for u in range(1, 6):
    print(f" Squares of the number {u} = {u*u}")
    time.sleep(1)