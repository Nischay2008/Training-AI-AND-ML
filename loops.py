for i in range(1,6):
    print (i)

word = "python"
for ch in word:
    print(ch)

total = 0
for i in range(1, 11):
    total += i
print("Sum:", total )

while True:
    word = input("Enter something (type 'exit' to stop) : ")
    if word == "exit" :
        break
    print("You entered:" ,word )


    for  i in range(1,6):
        if i == 3:
            continue
        print(i)