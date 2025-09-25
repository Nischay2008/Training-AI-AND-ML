def square(x):
    return x*x
numbers = [1,2,3,4,5]
squared = list(map(square, numbers))
print(squared)  



def is_even(x):
    return x % 2 == 0
numbers = [1,2,3,4,5,6]
even_numbers=list(filter(is_even,numbers))
print(even_numbers)

from functools import reduce

def add(x,y):
    return x + y
numbers1 = [1,2,3,4,5]
sum_numbers = reduce(add,numbers1)
print(sum_numbers)