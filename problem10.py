# Write a python program to print all the even numbers from 1 to 50.
import time


for i in range(1 , 50):
    if i % 2 == 0:
        print(i)
        time.sleep(0.1) 