'''
import time

for i in range(-10 , 10):
    if i/-1 <= 0:
        continue
    print(i)

print("Positive Numbers.")

for i in range(-10 , 10):
    if i <= 0:
        continue
    print(i)
print("")

for y in range(1 , 100):
    if y % 3 == 0:
        continue
    print(y)
    time.sleep(0.2)

print("List type.")

num  = [-1 , 2 , 3, 4, 5 , 6 , 7 -3 , -4 , 6 ,-5]

for nu in num:
    if nu < 0:
        continue
    print(nu)
print("")

num1 = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
for y in num1:
    if y % 3 == 0:
        continue
    print(y)

print("")

#while True:
 #   x = int(input("Enter a number: "))
  #  if x > 0:
   #     print("It is a postive number.")
    #elif x/-1 < 0:
     #   continue
print("")

for nuu in range(1,10):
    if nuu == 2:
        pass
    print("Number:", nuu)
'''

x = input("Type Yes or No").lower()
if x == "yes":
    print("Dunno")
    pass
else:
    print("No")

