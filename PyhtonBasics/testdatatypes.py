# Numbers  - integer and float  - used to store numeric values

a = 20

print(type(a))

print(len(str(a)))

b = 10.0

print(type(b))
# Complex integers
# i=20
# c = 50+10i
# print(type(c))

# Sequence data type:
# String list tuple
# String - collection of characters

# String
str1 = 'Welcome to Automation Testing'

print(str1)
# length of the string
print(len(str1))

# Type of variable
print(type(str1))

# print each character in the String
for i in range(0, len(str1)):
    print(str1[i])

# reverse the String
revstr = ''
for s in str1:
    revstr = s + revstr

print(revstr)

strsplit = str1.split(" ")  # 0 1 2 3
revword = ""
for w in range(0, len(strsplit)):
    revword = strsplit[w] + " " + revword

print(revword)

# List - list is a datatype, which allows multiples to store whether is it integer, string and boolean

list1 = ['10', 50, 80, 100, 5, 1, 7, True]
list2 = [10, 50, 80, 100, 5, 1, 7]

print(len(list1))  # length of the list

list1.append('sai charan')

print(type(list1))

print(list1)

print(list1[0:3])

print(list1[:3])
print(list1[3:])

print(list1 + list2)

print(list1 * 3)

print(list1[-1])
print(list1[3])

list1.insert(3, "venkat")  # inserting value to list based on index
print(list1)
list1[3] = "VENKAT"  # Updating list

print(list1)

del list1[3]

print(list1)

# Tuple -

tuple1 = (10, 20, 40, 85, 75)
tuple2 = (10, 20, 40, 85, "75", False)

print(len(tuple1))
print(type(tuple1))

# Tuple slicing
print(tuple1[1:])
print(tuple1[0:1])

# Tuple concatenation using + operator
print(tuple1 + tuple1)

# Tuple repatation using * operator
print(tuple1 * 3)

# Adding value to tup. It will throw an error.
#tuple1[2] = "hi"

# Difference between list and tuple

# list is a data type that store multiple values and same/different data types
# tuple is also same as list
# list is mutable, we can the change the values inside the list like adding, updating, deleting
# tuple is immutable, we cannot the change the values inside the tuple

# Dictionary:

# Dictionary is a order set of key pair value of items and where each key stores a specific value

dict = {"e":2,"b":30,"c":100,"d":500,"a":1}

print(len(dict))
print(dict)

print(type(dict))

dict["firstname"] = "venkat"
dict["lastname"] = "kandula"

print(dict)

print(len(dict))

del dict["b"]

print(dict)

print(dict["c"])

# Boolean

# Boolean can provide two builin data types True and False

# True can be Represent with T and False can be represent with F

flag = True

print(type(flag))

print(type(False))

# Set

# Set is a unorder set of collection of items, it is separted by the comma and enclosed by the {}
# It contains various types of values (different data types)

set1 = set()

set2 = {"Venkat",2,4,1,2,True, False, False, "kandula"}

print(set2)

set2.add("10")

print(set2)

set2.remove("kandula")

print(set2)

print(len(set2))

print(type(set2))





