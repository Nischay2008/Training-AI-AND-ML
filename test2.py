def main():
    print("4 Problem.")

    a = int(input("Enter value X: "))
    b = int(input("Enter value Y: "))
    c = int(input("Enter value Z: "))
    print(a, b, c)
    print( "The maximum is ",maximum(a, b, c))


def maximum(x, y, z):
    numbers = (x,  y, z)
    init = x
    for f in numbers:
        if f > init:
            init = f
    return init


main()

def main():
    text = input("Enter a word: ").lower()
    print(vowel(text))

def vowel(txt):
    vowels = ['a' , 'e' , 'i' , 'o' , 'u']
    count = 0
    for c in txt:
        if c in vowels:
            count += 1
    return count

main()

