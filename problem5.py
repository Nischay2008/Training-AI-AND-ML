# Create a program that takes an integer input and increments the value by 1 using the += operator and decreaments the value by 
# 1 using the -= operator.
import time

x = int(input("Enter the value of X: "))

j = x
i = 0

for i in range (1, x):
    i += 1
    print(f"i = {i}")
    time.sleep(0.1)

time.sleep(0.1)
while j >= 0:
    print(f"j = {j}")
    j -= 1
    time.sleep(0.1)