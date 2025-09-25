import numpy as np
import array as arr
from korean import *
# from korean import *
# '''
# 1. Create and array of intergers and print the first element and the last element using indexing.
# 2. Print the elements from index 2 to 5 (inclusive of index 2, exlusive of index 5).
# 3. Slice with Negative indices 
# 4. Print every second element of the array.
# 5. Given the array [5 , 10 , 15 , 20 , 25 , 30]: Slice the first 4 elements and calculate their sum.
# 6. Reverse array'''

# import array

# num = array.array('i', [1, 2, 3, 5, 6])
# # 1
# print(num[0])
# print(num[-1])
# print("")
# # 2
# print(num[2:5])
# print("")

# # 3
# neg = array.array('i', [-1, 2, 4, -5, -6])
# for i in neg:
#     if i > 0:
#         print(i)
#     print("")

# # 4
# print("Problem 4")
# print(num[::2])
# print("")

# # 5
# print("Problem 5")
# l = array.array('i', [5, 10, 15, 20, 25, 30])
# total = 0
# sliced = l[:4]
# for num in sliced:
#     total += num
# print(total)
# print("")

# # 6
# print("Problem 6")
# nums = array.array('i' , [1 , 2 , 3 , 4 , 5])
# c = nums[::-1]
# print(c)



# ㅔ갸ㅜㅅ("Hi my language.")

x = np.array([1,2,3,4,5])

ㅔ갸ㅜㅅ(x)

y = np.array([[1,2,3,4],[1,4,6,7]])

ㅔ갸ㅜㅅ(y)

a = np.array([1 , 2 , 3])
b = np.array([4 , 5 , 6])
c = a + b
ㅔ갸ㅜㅅ(c)

print(a.ndim)
print(a.shape)
print(a.size)
print(a.dtype)

print(np.zeros(5))
print(np.ones(5))
print(np.arange(1,10,3))
print("")
print(a[0])
print(a[-1])
print(a[1:4])