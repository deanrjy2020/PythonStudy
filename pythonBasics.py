#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Check the Tutorial for more examples.
# https://docs.python.org/3/tutorial/index.html

# input, to string automatically.
#name = input("Enter your name: ")
#print("Hello " + name)

# basic data type, int, float, string, bool/True/False, None, 

# to int/float
int("5")
float("5.2")
#to string
str(3) 
# %s can be used for EVERYTHING.
print("result is float: %f, result is integer (like C++): %d" % (10/3, 10//3) )#3.3333...

# r'' means the thing in '' works as string.
print(r'\n\t, test')
#encode, pythong is uding Unicode, but looks like the MINGW does not support Chinese. (Windows PowerShell is ok.)
print("Chinese character is: " + chr(25991) + ", encode of 中 = " + str(ord('中')) + ", A = " + str(ord("A")) )

# list
data = ["Mike", "Jone", 3, 4.5]
print("data = %s, size=%s" % (data, len(data)) )
data2 = ["Dean", True]
print("adding to the end: %s" % (data+data2) )
#use this way to remove the ones you don't like, copy to new.
print("ading to the middle: %s" %(data[:1] + data2 + data[1:]) ) 
#replace, and 2D list
data[0] = ["Michael", "Mathias"]
print(data)
#search the index
print(data.index("Jone"))

#tuple
# cannot be changed after initialized, otherwise same as list.
tuple_data = (1, "Mia", 5.5)
print("getting the data type: %s,%s,%s,%s,%s,%s," %(type("5.5"), type(5.5), type(5), type(True), type(data), type(tuple_data) ) )

#dictionary = map
map = {
    "key1" : "value1",
    "key2" : "value2",
    3 : 4
}
print(map)
#access value2
print(map["key2"])
print(map[3])

#set
my_set = set(data2)
print(my_set)
#search it as the string
print("Is \"Dean\" in the set? %s" % ("Dean" in my_set) )

# for loop
for i in range(3):
    print(i)

class Student:
    #constructor
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

stu1 = Student("Jon", 3.8)
print("student obj = %s, name=%s, gpa=%s, on_honor_roll? %s " %(stu1, stu1.name, stu1.gpa, stu1.on_honor_roll()))



print("Done.")
