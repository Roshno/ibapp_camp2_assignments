
import sys
from tkinter import SE
from tkinter.ttk import Separator 


print ("hello world")
#JUST PRINTING THE PYTHON VERSION
"""just a
multiline comment
print (sys.version)


# Exercise: Format and count
text = "{} is my country. All Indians are my brothers and sisters.".format('India')
print(text)

count = text.count('India')
print("Count of India in the text is {}".format(count))

myString = 'superman'
print(myString.endswith('man'))
#start checking from index 3 onwards
print(myString.endswith('man',3))
#start checking from index 2 to 6
print(myString.endswith('man',2,6))
#start checking from index 2 to 6
print(myString.endswith(('man','ma'),2,6))

myString = "Good Morning"
print(myString.find('Mo'))
print(myString.find('Mo',3))
print(myString.find('Mo',3,7))
print(myString.index('M0o'))

#join() method to join items in a tuple with a separator
Separator = '*'
myTuple = ('h','e','l','l','o')
myNewString = Separator.join(myTuple)
print(myNewString)
print(myNewString.lower())
print(myNewString.upper())


#replace and split methods
myString = "Hello World"
myString = myString.replace('o','i',1)
print(myString)

myStringSplit = myString.split(' ')
print(myStringSplit)

import re
txt = "bits of paper bits of paper"
x = re.findall("bi", txt)
print(x)

x = re.search("bi", txt)
print(x)

import re
txt = "bits of paper bits of paper"
x = re.split(" ", txt)
x = re.split(" ", txt,1)
print(x)

import re
txt = "bits of paper bits of paper"
x = re.sub(" ", "-", txt)
print(x)

x = re.sub(" ", "-", txt,1)
print(x)

#pattern search using metacharacters
import re
txt = "hello world"
#find all lower case characters alphabetically between a and m
x = re.findall("[a-m]", txt)
print(x)

txt = "James Bond is 007"
#find all the digits
x = re.findall("\d", txt)
print(x)
#check for a substring starting with J and has
three characters between and ends with s
x = re.findall("J...s",txt)
print(x)

#check if string starts with 'hello'
using the metacharacter
import re
txt = "hellohi world"
x = re.findall("^hello",txt)
print(x)
#check if string ends with 'world'
x = re.findall("world$",txt)
print(x)


import re
txt = "James bond is 007"
x = re.findall("\AJam", txt)
print(x)

#check if string starts with 'James'
#using the metacharacter
txt = "The James Watt invented the engine"
#look for a substring with 'Jam'
x = re.findall("\AJam", txt)
print(x)


import re
#check if string ends with 'the'
#does not matter if 'the' is a word or part of word
#using the metacharacter $
txt = "James Watt invented the"
#look for a substring with 'Jam'
x = re.findall(r"the$", txt)
print(x)


#check if ANY OF THE WORD in the string starts with 'the'
#using the special sequence \b
txt = "James Watt invented theso"
#r is for raw string
x = re.findall(r"\bthe", txt)
print(x)

#matching an email within a string using special sequence
import re
myString = "my email is roshni@gmail.com hope you will note it down"
#regular expression to match email
#check for non space chars before and after '@'
regex = '\S+@\S+'
x = re.findall(regex, myString)
print(x)


#Python LISTS and list access options
studentsAge = [18,21,23,20,21]
print(studentsAge)
print(studentsAge[2]) #print particular index
newstudentsAge = studentsAge[2:4] #starting from 2 till 4-1
print(newstudentsAge)
newstudentsAge = studentsAge[1:5:2] #starting from 1 till 5-1,every second element
print(newstudentsAge)
newstudentsAge = studentsAge[:3] #starting from 0 index till 3-1
print(newstudentsAge)
newstudentsAge = studentsAge[::-1] #reverse the list
print(newstudentsAge)
newstudentsAge = studentsAge[-1] #reverse the list
print(newstudentsAge)

#append to add a value to the end of the list
studentsAge.append(16)
studentsAge.append("hi")
print(studentsAge)
#delete values from the list
del studentsAge[-1]
print(studentsAge)

#combine two lists using extend()
studentsName = ['Anu','Binu','Sinu']
studentsAge.extend(studentsName)
print(studentsAge)

#to check if a variable is in the list using 'in' operator
print('Anu' in studentsName) 
print('Anushka' in studentsName) 
#get the no of items in the list
print(len(studentsName))
print(len(studentsAge))

#reverse the contents of the list destructively
studentsName.reverse()
print(studentsName)
studentsName.reverse()
print(studentsName)

#list concatenation using + operator
print(studentsName + studentsName)
print(studentsName)

#list duplication/multiplication using * operator
print(studentsName*2)
4

NumList = []

Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

NumList.sort()

print("Element After Sorting List in Ascending Order is : ", NumList)

"""
#1. sort list in ascending order
numbers = [1, 3, 4, 2]
# Sorting list of Integers in ascending
numbers.sort()
print(numbers)
print(numbers[0])

#2. to find second largest number in list
list1 = [10, 20, 4, 45, 99]
list1.sort()
print("Second largest element is:", sorted(list1)[-2])

#3. print odd numbers and even numbers separately in a list of [1,2,3,4,5,6,7,8,9,10]
list2 = [1,2,3,4,5,6,7,8,9,10]
even_list=[]
odd_list=[]
for i in range(len(list2)):
  if(list2[i]%2==0):
    even_list.append(list2[i])
  else:
    odd_list.append(list2[i])
print("Even Numbers List:", even_list)
print("Odd Numbers List:", odd_list)

#4. program for reversing a list
list1 = [10, 20, 4, 45, 99]
list1.reverse()
print(list1)

#5. program to print all odd numbers from 1-50
start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))
for num in range(start, end + 1):
     
    # checking condition
    if num % 2 != 0:
        print(num, end = " ")


#6.create a list that contains only Even numbers in given range
even_list = range(start, end + 1)[start%2::2]
 
for num in even_list:
    print(num, end = " ")

#7. program to count even and odd numbers in a list
list1 = [10, 21, 4, 45, 66, 93, 11]
  
odd = [num for num in list1 if num % 2 == 1]
odd_count = len(odd)
  
print("Even numbers in the list: ", len(list1) - odd_count)
print("Odd numbers in the list: ", odd_count)

#8. write a python program to remove zeros from an IP address
import re
IP = "216.08.094.196"
string = re.sub('\.[0]*', '.', IP)
print(string)

#9. Write a python program that matches a string that has an 'a' followed by anything, ending in'b'
txt = 'I have a limb'
res=re.findall(".*a.*b",txt)
print(res)

#10. 
string = 'They ate 6 apples and 10 bananas'
string = re.sub('6', 'six', string)
string = re.sub('10', 'ten', string)
print (string)
List = [1,2]