code = """
print("hello)
"""

try:
    exec(code)
except SyntaxError:
    print("You have made a mistake")
finally:
    print("You know what is common in your code. It is a error.")
    
try:
    print(10/0)
except ZeroDivisionError:
    print("Invalid Entries")
finally:
    print("Nice bro you have reached the end.")

try:
    x = "k"
    y = input("enter: ")
    if y not in x:
        raise ValueError
except ValueError:
    print("Wrong input")
finally:
    print("Done right.")

try:
    b = int("Okay")
    print(b)
except ValueError:
    print(f"Ik you wanted to print {b}. But it should not be in int bro.")
finally:
    print("Done coding.")

# try: 
#     f = open("trump.txt")
# except Exception as e:
#     print("Error:" , e)
# finally:
#     print("File handling failed.")