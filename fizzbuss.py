import time

i = 1
fizz = 0
buzz = 0
fizzbuzz = 0

while i <= 10000:
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i} FIZZBUZZ")
        fizzbuzz += 1
    elif i % 3 == 0 and i % 5 != 0:
        print(f"{i} FIZZ")
        fizz += 1
    elif i % 3 != 0 and i % 5 == 0:
        print(f"{i} BUZZ")
        buzz += 1
    else:
        print(i)

    i += 1
    time.sleep(0.001)

print(f"Fizz : {fizz} , Buzz : {buzz} , FizzBuzz : {fizzbuzz} ")
