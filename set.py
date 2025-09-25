se = {1, 2, 3, 4, 5, 6,  7}
print(se)
se.add(8)
se.remove(7)

student = {
    'name': 'Nischay',
    'age': '17',
    'grade':'A',
    'class':'AI&ML-E',
    'course':'CSM(Cse-Ai&Ml)'
}
print(student)
print(student['name'])
student['Blood Group'] = 'O+ve'
print(student)

my_list = [1 , 2 , 3 , 4 , 4]
my_tuple = tuple(my_list)
print(f"The list {my_list} is changed to Tuple {my_tuple}")

x = list(student.values())
y = list(student.keys())
print(x)
print(y)

xx = {1 , 2 , 4}
u = list(xx)
print(u)
a = list(my_tuple)
print(a)

import array

numbers = array.array('i' , [1,2,3,4,5])
print(numbers)

floats = array.array('f' , [1.1,1.2,2.2,3.3])
print(floats)

print(numbers[0])
print(numbers[1:4])
print(numbers[::-1])
o = numbers.append(6)
print(o)
numbers.insert(1,10)
print(len(numbers))
print(sum(numbers))
print(max(numbers))
print(min(numbers))
numbers.remove(1)
print(numbers)
del numbers[2]
print(numbers)


user = input("뚯ㄷㄱ ㅛㅐㅕㄱ ㅏㅐㄱㄷ무 ㅜ믇(Enter your username): ")
korean = ["ㅜㅑㄴ초묘" , "냐옴ㅁㄱㅇ" , "ㄲ도ㅡ무" , "냑"]
if user not in korean:
    raise ValueError("ㅑㅜㅍ미ㅑㅇ ㅕㄴㄷ구믇(Invalid Username)")
passw = input("뚯ㄷㄱ ㅛㅐㅕㄱ ㅔㅁㄴㄴ잭ㅇ(Enter your password) : ")
passw_u = ["ㅜㅑㄴ초묘@123" , "ㅡㄲㅊㄸㅆ"]
if passw not in passw_u:
    raise ValueError("ㅑㅜㅍ미ㅑㅇ ㅖㅁㄴㄴ잭ㄴ(Invalid Password)")
print("ㅛㅐㅕ ㅗㅁㅍㄷ 녗ㅊㄷㄴ려ㅣㅣㅛ ㅣㅐ햐ㅜㄷㅇ(Logined.)")

