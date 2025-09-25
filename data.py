with open('trump.txt', 'r') as file:
    print(file.read(5))              # read first 5 chars
    print("Pointer at:", file.tell())  # pointer position
    file.seek(0)                     # reset pointer
    print(file.read())               # read whole file again
