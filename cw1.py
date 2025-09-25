names = ['Yugamate' , 'Dynamate' , 'Sodamate' , 'Cremate' , 'Buslate' , 'Neonmate' , 'Classymate']

#import time

print(names)
print("")
#time.sleep(0.5)
names.append('Buzzmate')
print(names)
print("")
#time.sleep(0.5)
names.remove('Neonmate')
print("")
#time.sleep(0.5)
names[1] = 'Sodamate'
print("")
#time.sleep(0.5)
print(names)
print("")
#time.sleep(0.5)
print(names[0])
print("")
#time.sleep(0.5)
print(names[-1])
print("")
#time.sleep(0.5)
roll_numbers = [258 , 260 , 259 , 257]
roll_numbers.sort()
print(roll_numbers)


print("")

verify = input("Enter the name : ").capitalize()
if verify in names:
    print(f"The {verify} is present in the list.")
else:
    print(f"The {verify} is not present in the list.")

print("")

Colours = ("Blue" , "Red" , "Green")
print(Colours)

print("")

print(Colours[0])
print("")
print(Colours[-1])

print(names[:3])
print(names[2:])
print(names[::2])
print(names[:-1])

x = names.index('Yugamate')
print(x)
c =names.count('Yugamate')
print(c)


for number in range(1,10):
    if number == 5:
        print("Breaking the loop at number 5")
        break
    print("Number:" , number)