"""
import sys
from tkinter import SE
from tkinter.tix import DisplayStyle
from tkinter.ttk import Separator 


print ("hello world")
#JUST PRINTING THE PYTHON VERSION
just a
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


#Tuples in Python
months = ("Jan","Feb","March")
print(months[0])
print(months[-1])
#months[0] = "test" will not work

#tuples methods in python
print(len(months))
print("Jan" in months)
print("January" in months)
#del months
print(months)
print(months+months)
print(months*3)


#dictionary in python
#dictionary declaration
#method1
myStudents = {"Abhi":30, "Sibi":28, "Subi":"not updated"}
print(myStudents)
#method2
myStudents = dict(Abhi=30, Sibi=28, Subi="not updated")
print(myStudents)
#method3
myStudents = dict({"Abhi":30, "Sibi":28, "Subi":"not updated"})
print(myStudents)
print(myStudents["Sibi"])

#Dictionary methods
print(myStudents.get("Subi"))#will return corressponding value
print(myStudents.items()) #will return dict items as array of tuples
print(myStudents.keys()) #return keys of the dict
print(myStudents.values()) #return values of the dict
print("Abhi" in myStudents) #check if value is present
print(30 in myStudents.values()) #check if value is present
print(len(myStudents))

myStudents2 = {"Abhi": 31, "Binu": 26}
myStudents.update(myStudents2)#join together dict by overwriting duplicate keys
print(myStudents)

myStudents.clear() #clear all values inside dict
print(myStudents)

del myStudents #delete dict along with variable
print(myStudents)


#Set in python

#method1
months = {"Jan","Feb","March"}
#method2 
months = set(["Jan","Feb","March"])

print(months)
print(type(months))

#looping thriugh elements in a set
for i in months:
    print(i)

#declare an empty set
days = set()
#add values to set
days.add("Mon") #insert single values
days.add("Tue")
days.add("Wed")
#looping thriugh elements in a set
for i in days:
    print(i)

days.update(["Thur","Fri"]) #insert multiple items
#looping thriugh elements in a set
for i in days:
    print(i)

#remove items from the set
#using discard() method, will remove item, not display error if item does not exist
days.discard("Thur")
for i in days:
    print(i)

#using remove() method, will remove item, will display error if item does not exist
days.remove("Thur")
#loop through items in set
for day in days:
    print(day)

days.clear()
print("cleared the set")
for day in days:
    print(day)
  

#set operations
months1 = {"Jan","Feb","Mar"}
months2 = set(["Mar","Apr","May"])
#union operation
months4 = months1 | months2
print(months4)
for month in months4:
    print(month)

#intersection operation
months4 = months1 & months2
print(months4)

#intersection update
months1 = {"Jan","Feb","Mar"}
months2 = {"Mar","Apr","May","Feb"}
months3 = {"Feb","Mar","Jun","Jul"}
#months1.intersection_update(months2,months3)
#print(months1)

#difference operation
months4 = months1 - months2
print(months4)

#symmetric difference 
#will retain all elements of set excluding the common ones
months4 = months1 ^ months2
months4 = months1.symmetric_difference(months2)
print(months4)

#Set comparisons operation
months1 = {"Jan","Feb","Mar","Apr","May","Jun"}
months2 = {"Mar","Apr","May","Feb"}
months3 = {"Feb","Mar","Jun","Jul"}
#checking if months1 is a superset of months2
months1 > months2
print(months1 >months2)
print(months1 <months2)
#check if two sets are equal
print(months2 == months3)
#check if two sets are equal
print(months1 >= months2)
#check if two sets are equal as well as month2 is a superset of month1
print(months1 <= months2)

#frozen set
months4frozen = frozenset(["Nov","Dec"]) #immutable set
print(type(months4frozen))
print(months4frozen)

months4frozen.add("oct") #frozen set has no attribute

#input and output functions in python
studName = input("Please enter you name: ")
studAge = input("Please enter you age: ")
print(studName)
print(type(studName))
print(studAge)
print(type(studAge))

#variations of print statement to include variables
print("The student name is",studName, "and the age is",studAge)
print("The student name is %s and the age is %s" %(studName,studAge))
print("The student name is {} and the age is {}" .format(studName,studAge))

#print in multiple lines
print('''Hello World
How are you''')
#print a new line
print("Hello World\nHow are you")
print("This is a backslash\\")
print('I am 5\' 5\" tall')

#control flow ststement
#conditional statements
#if condition
userInputNo = input('Enter either 1 or 2:')
if(userInputNo == "1"):
    print("You entered 1")
    print("And you are number 1")
elif(userInputNo == "2"):
    print("You entered 2")
    print("Runner up. Keep it up!")
else:
    print("you did not enter 1 or 2")

#inline if statement
B=12
A=12 if B==10 else 13
print(A)

print("B is ten" if B==10 else "B is not 10")

#oython match case statement example
#define a function

def http_status(status):
  match status:
    case 400:
      return "Bad Request"
    case 404:
      return "Page not found"
    case _:
      return "Unknown error occured"
#calling the function inside print statement
print(http_status(404))


userInputMonth = input('Enter DOB month number:')
if(userInputMonth == "1"):
    print("Garnet")
    print("People born in January are bold and alert")
elif(userInputMonth == "2"):
    print("Amethyst")
    print("People born in February are lucky and loyal")
elif(userInputMonth == "3"):
    print("Aquamarine")
    print("People born in March are naughty and gentle")
elif(userInputMonth == "4"):
    print("Diamond")
    print("People born in April are caring and strong")
elif(userInputMonth == "5"):
    print("Emarld")
    print("People born in May are kucky and practical")
elif(userInputMonth == "6"):
    print("Alexandrite")
    print("People born in June are romantic and curious")
elif(userInputMonth == "7"):
    print("Ruby")
    print("People born in July are adventurous and honest")
elif(userInputMonth == "8"):
    print("Peridot")
    print("People born in August are active and hardworking")
elif(userInputMonth == "9"):
    print("Sapphire")
    print("People born in September are romantic and pretty")
elif(userInputMonth == "10"):
    print("Toumaline")
    print("People born in October are stylish and friendly")
elif(userInputMonth == "11"):
    print("Citrine")
    print("People born in November are nice and creative")
elif(userInputMonth == "12"):
    print("Zircon")
    print("People born in December are nice and creative")
else:
    print("invalid number")


match (userInputMonth):
    case '1':
      print( "Garnet\nPeople born in January are bold and alert")
    case '2':
      print( "Amethyst\nPeople born in February are lucky and loyal")
    case '3':
      print( "Aquamarine\nPeople born in March are naughty and gentle")
    case '4':
      print("Diamond\nPeople born in April are caring and strong")
    case '5':
      print("Emarld\nPeople born in May are kucky and practical")
    case '6':
      print( "Alexandrite\nPeople born in June are romantic and curious")
    case '7':
      print( "Ruby\nPeople born in July are adventurous and honest")
    case '8':
      print("Peridot\nPeople born in August are active and hardworking")
    case '9':
      print("Sapphire\nPeople born in September are romantic and pretty")
    case '10':
      print("Toumaline\nPeople born in October are stylish and friendly")
    case '11':
      print("Citrine\nPeople born in November are nice and creative")
    case '12':
      print("Zircon\nPeople born in December are nice and creative")
    case _:
      print("Unknown error occured")
  

#looping in python
#FOR loop to loop/iterate through a list in python
fruits = ['apples','oranges','banana','cherry']
for fruit in fruits:
  print (fruit)

#to display index using the enumerate method
for index, fruit in enumerate(fruits):
  print(index,fruit)

#tuse for loop to generate a series of numbers
#using the range function
for i in range(10):
  print(i)

#WHILE loop
counter = 5
while counter > 0:
  print ("Counter =", counter)
  counter = counter - 1

#break and continue statements
#break example
j = 0
for i in range(10):
  j= j +2
  print('i = ', i,'j = ', j)
  if j ==6:
    break
  print()

#continue example
j = 0
for i in range(10):
  j= j +2
  print('i = ', i,'j = ', j)
  if j ==6:
    continue
  print('continue j value is:',j)

#try except statement (similar to try catch) in python
try:
  answer = 12/0
  print(answer)
except:
  print("Some friendly error message")


#print list of numbers multiples of 5 and divisible by 8
start = int(2000)
end = int(2500)
count = start
while count <= end:
    if count % 5 == 0 and count % 8 == 0:
        print(count, " is divisible by 5 and 8.")
    count = count + 1 

#print multilication tables
num = int(input("Enter number"))
for i in range(1,11):
  print(num, 'x',i,'=',num*i)
          

#functions in python
def findSum(a,b):
  sum = a + b
  return sum
print(findSum(2,3))

#define the function
def checkIfPrime(numberToCheck):
  for x in range(2,numberToCheck):
    if(numberToCheck % x == 0):
      return False
  return True
print(checkIfPrime(5))
print(checkIfPrime(15))

#function returning multiple values
def calculations(a,b):
  add = a + b
  sub = a - b
  mul = a * b
  div = a % b 
  return(add,sub,mul,div)
#calling the function
output = calculations(40,30)
print("Add result",output[0])
print("Sub result",output[1])
print("Mul result",output[2])
print("Div result",output[3])

#generator is a function that returns an iterator
#iterator is something that we can loop through using a looping statement
def calculationsyield(a,b):
  add = a + b
  yield add
  sub = a - b
  yield sub
  mul = a * b
  yield mul
  div = a % b 
  yield div

#using a for loop we can loop through the returned value from the function
for value in calculationsyield(30,40):
  print (value)


#Demonstrating the variables scope
#Declaring a global variable
message1 = "Just a global variable"

def myFunction():
  global message1 #enable modification of global variable inside the function
  print("Reached inside function")
  print(message1) #printing the global variable
  message2 = "Its a local variable" #declaring local variable
  print(message2)
  message1 = "Just modifying the global variable"
  print(message1) #printing the global variable

myFunction() #calling the function
#print(message1)
#print(message2)

#demonstrate an arbitary list of arguments into the function
def make_pizza(size, *toppings): #arbitrary list parameter is prefixed by *
  print(f"\nMaking a {size} -inch pizza with following toppings:")
  for topping in toppings:
    print(f"\n{topping}")

make_pizza(12,"pepperoni")
make_pizza(16,"mushroom","green pepper")

def printinfo(name, age):
  print("Name: ", name)
  print("Age: ", age)
  
#calling with required arguments
printinfo("Tom", 17)
#calling with keyword arguments
printinfo(age=17, name ="Minnie")

#Anonymous Functions
#LAMBDA

sum = lambda num1, num2: num1 + num2
#calling the lambda function
print("sum of two numbers ",sum(2,3))


#python modules
#importing a module
import random
#calling function inside the module
print(random.randrange(1,10))

import random as r
#calling function inside the module
print(r.randrange(1,10))

from random import randint, randrange
print(randrange(1,10))

#random built in module
import random
print(random.random())
print(random.randint(5,20))
print(random.choice(["head", "tail"]))
myShirtColors = ["blue","red","black","yellow","green"]
random.shuffle(myShirtColors)
print(myShirtColors)

random.seed(10)
print(random.random())
random.seed(11)
print(random.random())

#python date time module
import time
print(time.time()) #seconds past 1st Jan 1970
print(time.localtime(time.time())) #get the multiple time valus as a tuple
print(time.asctime(time.localtime(time.time())))

for i in range(0,10):
  print(i)
  time.sleep(1) #delay program executio by the specified number of seconds


import datetime
print(datetime.datetime.now()) #return the current date time object

#creating custom datetime object
birthDay = datetime.datetime(2022,7,20)
print(birthDay)
birthDay = datetime.datetime(2022,7,20,10,15,50)
print(birthDay)

#time comparison demo
from datetime import datetime as dt

if dt(dt.now().year,dt.now().month,dt.now().day,9)< dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,18):
    print("Working now")
else:
    print("Shift completed")

import calendar
myCalendar = calendar.month(2022,7) #get calendar for a month
print(myCalendar)
myCalendar = calendar.prcal(2022) #get calendar for a year
print(myCalendar)

import math
#finding the exponential of a number, then its absolute, then its log, then
#convert to the base of 10
number = 2e-7 
print(math.log(math.fabs(number),10))

number = math.pow(4,2) #4 to the power of 2
print(number)
number = math.floor(4.2) #round to the smallest digit
print(number)
number = math.ceil(4.2) #round to the next digit
print(number)
number = math.fabs(-10) #return absolute value
print(number)
number = math.factorial(10) #return factorial
print(number)
number = math.modf(3.14) #return int anf fractional part
print(number)


#calling the custom module created
import prime
answer = prime.checkIfPrime(10)
print(answer)
"""





def calculateGstShare(price, rate):
    return price * (rate / 2) / 100
def printGstDetails():
    SGST = CGST = calculateGstShare(price, rate)
    print("Actual price of the item :", price)
    print("Price after applying CGST :", CGST)
    print("Price after applying SGST :", SGST)
    print("Total price with GST :", price + CGST + SGST)
price = float(input("Price before GST : "))
rate = float(input("GST rate : "))

printGstDetails()














