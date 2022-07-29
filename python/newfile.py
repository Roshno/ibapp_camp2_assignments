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




#rights of a function in python
#is similar to the rights of a variable
#1 we can assign a function to a variable
import re


def myFunc1():
  print("This is my function 1")

#assign the function to a variable
myMyFunction = myFunc1

myFunc1() #call function directly
myMyFunction() #CALL THE FUNCTION VIA THE VARIABLE

#2 we can pass a function as an argument into another function
def myFunc2(receivedFn):
  receivedFn()
  receivedFn()

myFunc2(myFunc1)
  
#3 we can return a function from another function
def returnToUpperFn():
  return str.upper

upperRef = returnToUpperFn()
print(upperRef("hello world"))

#4 we can define a function inside another function
def outer():
  print("outer function")

  def firstInner():
    print("first inner function")

  def secondInner():
    print("second inner function")

  firstInner()
  secondInner()

outer()

#5 inner functions can access variables in the enclosing function
def myOuter(myGreeting):
  print("The outer function says ",myGreeting)

  def myfirstInnerFunc():
    print("The first inner function says ",myGreeting)
  
  return myfirstInnerFunc

myOuterFunVariable = myOuter("Peace to the world")
myOuterFunVariable()


#21-07-2020

#python decorator
#a function which accepts another function, enhance it 
#with a wrapper function and return enhanced function back

#define the decorator, which accepts another function as the argument
def myDecorator(myFunc):
  def myInnerWrapper(): #wrapper fn "decorates" the function received
    print("Just before the received function call")
    myFunc()
    print("Just after the received function call")
  return myInnerWrapper

#defining a simple fn to pass into the behavior

def myFnToPassIntoDecorator():
  print("A simple function to pass into decorator")

#calling the decorator
myDecoratorDemo = myDecorator(myFnToPassIntoDecorator)
#execute the decorator 
myDecoratorDemo()

#defining another simple function to pass into decorator
@myDecorator
def newmyFnToPassIntoDecorator():
  print("A simple function to pass into decorator")

newmyFnToPassIntoDecorator()


#Define a simple class witha constructor that can accept two variables
class Employee:
  #defining a global variable (data member)
  empCount = 0

  #defining a constructor
  #that can accept two values, name and salary
  #save those values into self (self is an instance of the class)
  def __init__(self, name, salary):
    self.name = name
    self.salary = salary
    Employee.empCount += 1 #increment the emp count when a new object is created

  #define a simple member function
  def displayEmpCount(self):
    print("Total no of employees:",Employee.empCount)
  #define another simple member function
  def displayEmployeeDetails(self):
    print("Name:",self.name)
    print("Salary:",self.salary)

#create an object of employee class
employee1 = Employee("Tom",2000)
#calling the function using the object
employee1.displayEmpCount()
employee1.displayEmployeeDetails()

#create an object of employee class
employee2 = Employee("Jerry",3000)
#calling the function using the object
employee2.displayEmpCount()
employee2.displayEmployeeDetails()

#accessing the variable directly from the class 
print("Total employee count:", Employee.empCount)


#demonstarting class inheritance
#defining the base class
class Rocket:
  #defining the constructor
  def __init__(self,name,distance):
    self.name = name
    self.distance = distance
    self.__myPrivateVar = ""
  #defining a member function which returns a string
  def launch(self):
    return "%s has reached %s" %(self.name, self.distance)

#Defining a derived class
class MarsRover(Rocket): #inherit from the base class
  def __init__(self, name, distance, maker, vehicleCode):
    Rocket.__init__(self, name, distance) #calling the base class constructor
    self.maker = maker
    self.__vehicleCode = vehicleCode #define a private variable using double underscores

  def printMaker(self):
    return "%s launched by %s"%(self.name, self.maker)
  
  def getVehicleCode(self):
    return self.__vehicleCode

class plutoRover(MarsRover):
  def getVehicleCode(self):
    return super().getVehicleCode()

#create object (instance) for main class Rocket
x = Rocket("Small rocket","till stratosphere")
y = MarsRover("Mars rover","till mars","ISRO","12345")
z = plutoRover()
print(z.getVehicleCode)

print(x.launch())
print(y.launch())
print(y.printMaker())
#due to encapsulation, we cannot access a private variable directly
print(y.__vehicleCode())
#this is the proper way of accessing a member variable
print(y.getVehicleCode())

#typically when using a decorator, it will return the name,doctsring etc
#of the wrapper function.
#to change this behavior and get the actual passed function's name and doc

#define the decorator, which accepts another function as the argument
#inside the decorator using another decorator 'wraps' before the wrapper function
import functools

def acceptDecorator(myString3):
  def myDecorator(myFunc):
    @functools.wraps(myFunc)
    def myInnerWrapper(*args): #wrapper fn "decorates" the function received
      print("Just before the received function call "+myString3)
      value = myFunc(*args)
      print("Just after the received function call")
      return value
    return myInnerWrapper
  return myDecorator


#defining another simple function to pass into decorator
@acceptDecorator("testing string into decorator")
def newmyFnToPassIntoDecorator(myString,myString2):
  Sample doc string for our newmyFnToPassIntoDecorator()function
  returnString = ("A simple function to pass into decorator "+ myString + myString2)
  return returnString

returnedString = newmyFnToPassIntoDecorator("just some test string"," next string")
print(returnedString)


#demonstrating class separating methods in python
#defining the main class

from cgi import print_exception


class Hero:
  #define the decorator @classmethod
  @classmethod
  def say_class_hello(cls): #since its class method, recieve as reference as implicit firdt argument
    if(cls.__name__ =="HeroSon"):
      print("Hi Prince, called from HerSon")
    elif(cls.__name__=="HerDaughter"):
      print("Hi Princess, called from HerDaughter")

  #define the decorator @staticmethod
  @staticmethod
  def say_hello():
    print("Hello...")
  
class HeroSon(Hero):
  def say_son_hello(self): #first implicit arg will be self since its a regular method
    print("Hello son from sub class HeroSon")

class HeroDaughter(Hero):
  def say_son_hello(self): #first implicit arg will be self since its a regular method
    print("Hello daughter from sub class HeroDaughter")

testHeroSon = HeroSon()
testHeroSon.say_class_hello()
testHeroSon.say_hello()

testHeroDaughter = HeroDaughter()  
testHeroDaughter.say_class_hello()
testHeroDaughter.say_hello()




#demonstrating class decorating mathod in python
#defining the main class
class Hero:
  #define the decorator @classmethod
  @classmethod
  def say_class_hello(cls): #since its classmethod, will receive class 
    if(cls.__name__=="HeroSon"):
      print("Hi Prince, calling from HeroSon")
    elif(cls.__name__=="HeroDaughter"):
      print("Hi Princess, calling from HeroDaughter")

  @staticmethod
  def say_hello():
    print("hello..")
class HeroSon(Hero):
  def say_son_hello(self):
    print("hello son from sub class HeroSon")

class HeroDaughter(Hero):
  def say_son_hello(self):
    print("hello daughter from sub class HeroDaughter")

testHeroSon = HeroSon()
testHeroSon.say_class_hello()
testHeroSon.say_hello()

testHeroDaughter = HeroDaughter()
testHeroDaughter.say_class_hello()
testHeroDaughter.say_hello()



class House:
  #constructor
    def __init__(self,price):
      self.__price = price #keeping price as private __price

  #creating the getter method with the property decorator
    @property
    def price(self):
      return self.__price
    
    #creating a setter method decorator, for fetching the attribute value in a class
    @price.setter
    def price(self, new_price):
      self.__price = new_price

    @price.deleter
    def price(self):
      del self.__price


#typical access and update will be like this:
house = House(500000) #create obj
print(house.price) #access attributes
house.price = 1000000 #modifying the attributes
print(house.price) #access attributes
del house.price #delete price of the house instance
print(house.price) #access attributes

#file handling demo using python
#trying to open a file myfile.txt in the same dir
myFile = open("myfile.txt","r")
#to read contents use read 
#print(myFile.read(10))
print(myFile.readline())
print(myFile.readline())
print(myFile.readline())




#a simple example for higher order function
#which can accept atleast one fn and can optionally return a fn

#a simple fn with a print statement
from tkinter import Y


def greet(name):
  return "Hello {}".format(name)

#defining the higher order fn which can accept fn
def print_greetings(fn,param):
  print(fn(param))

#calling the higher order fn
print_greetings(greet,"Roshni")

#map() function - a higher order fn which can accept a function and also
#a list of iterable parameters. Each param will be applied to the function 
#and result will be returned back as a map object.
#we can later convert this map object into a set/tuple.

#defining a simple function
def mymapfunction(a):
  return a*a

#calling the map function, passing the function as well as the iterables
x = map(mymapfunction, (1,2,3,4))
#x is a map object , need to convert that into a set/tuple
print(tuple(x))

# passing a lambda function as well as the iterables
x = map(lambda x: x*x, (1,2,3,4))
#x is a map object , need to convert that into a set/tuple
print(tuple(x))


#filter function which filters the iterables based on condition
#it accepts the fn and also the iterables as parameters

#defining a filter condition function
def filterfunc(x):
  if x>=3:
    return x

#calling the filter fn passing the condition fn and iterables
y = filter(filterfunc, (1,2,3,4))
#converting the returned filter obj into tuple/list/set etc
print(list(y))

#calling the filter fn passing the lambda fn and iterables
y = filter(lambda x: (x>=3), (1,2,3,4))
#converting the returned filter obj into tuple/list/set etc
print(list(y))


#reduce fn to reduce the list of values based on the operation we give
#it will accept the fn (preferaable lambda) fn and  the iterables
from functools import reduce
x = reduce(lambda a,b: a+b, [23,21,45,98])
print(x)

#class and regular unction without abstract classs
class Lion:
  def give_food(self):
    print("Feeding a lion with raw meat.")

class Panda:
  def feed_animal(self):
    print("Feeding a panda with bamboo.")

class Snake:
  def feed_snake(self):
    print("Feeding a snake with mice.")

#creating objects for animals we plan to feed:
simba = Lion()
kungfupanda = Panda()
kingcobra = Snake()

#calling the feeding fun for each of them
simba.give_food()
kungfupanda.feed_animal()
kingcobra.feed_snake()


from abc import ABC, abstractmethod
#ABC is Abstract Base Class
# from abc module, we have to import ABC and decorator abstractmethod

class Animal(ABC): #inherit from ABC
    @abstractmethod
    def feed(self):
      pass  #pass statement is a placeholder for future code
    
    #define a diet property using property decorator
    #and abstract method
    @property
    @abstractmethod
    def diet(self): #define diet ppty
      pass

    @property
    def food_eaten(self):
      #define food_eaten ppty
      #food_eaten ppty's getter
      return self.__food
      
    #having the setter for food_eaten
    @food_eaten.setter
    def food_eaten(self, food):
      if food in self.diet:
        self.__food = food
      else:
        raise ValueError(f"This animal does not eat this.")

    @abstractmethod
    def do(self,action):
      pass
  
  
#class and regular unction without abstract classs
class Lion(Animal):
  @property
  def diet(self):
    return ["antelope","chettah", "buffalo"]
  def feed(self): #must implement feed because its abs method
    print(f"Feeding a lion with {self.food_eaten}.")
  def do(self,action,time):
    print(f"{action} a lion with raw meat at {time}.")


class Panda(Animal):
  @property
  def diet(self):
    return ["bamboo","leaves"]
  def feed(self):
    print(f"Feeding a panda with {self.food_eaten}.")
  def do(self,action,time):
    print(f"{action} a panda with bamboo at {time}.")


class Snake(Animal):
  @property
  def diet(self):
    return ["mice","rabbit"]
  def feed(self):
    print(f"Feeding a snake with {self.food_eaten}.")
  def do(self,action,time):
    print(f"{action} a snake with mice at {time}.")


#creating objects for animals we plan to feed:
simba = Lion()
simba.food_eaten = "buffalo"
simba.feed()

kungfupanda = Panda()
kungfupanda.food_eaten = "bamboo"
kungfupanda.feed()

kingcobra = Snake()
kingcobra.food_eaten = "mice"
kingcobra.feed()

#file handling demo using python
#trying to open a file myfile.txt in the same dir
myFile = open("myfile.txt","r")
#to read contents use read 
#print(myFile.read(10))
#print(myFile.readline())
#print(myFile.readline())
#print(myFile.readline())

#reading the contents of thr file line by line using for loop
for line in myFile:
  print(line)

#we need to close the file cursor/obj once we completed 
#the operation associated with it.
myFile.close()

myFile = open("myfile.txt","r")
#read all the lines and return it as list
myFileContentsList = myFile.readlines()
print(myFileContentsList)
myFile.close()

#opening file cursor in append mode
myFile = open("myfile.txt","a")
#write() method is used to write text/data to the file
myFile.write("Humpty Dumpty sat on a wall\n")
myFile.close()

#opening file cursor in write mode
myFile = open("myfile.txt","w")
#write() method is used to write text/data to the file
myFile.write("Humpty Dumpty sat on a wall\n")
myFile.close()

myFile = open("myfile.txt","r")
print("The file pointer is now at ",myFile.tell())
#read all the lines and return it as list
#myFileContentsList = myFile.readlines()
#print("the file pointer is now at ",myFile.tell())
#print(myFileContentsList)
#print(myFile.readline())
#change the file pointer offset using seek()
myFile.seek(30)
print("The file pointer is now at ",myFile.tell())
myFileContentsList = myFile.readlines()
print("The file pointer is now at ",myFile.tell())
print(myFileContentsList)
myFile.close()

#renameing a file using python os module 
import os
if os.path.exists("myfilenew.txt"):
  os.rename("myfilenew.txt","myfile.txt")
  print("rename success")
else:
  print("This file does not exist")


if os.path.exists("myfilenew.txt"):
  os.remove("myfile.txt")
  print("renmove success")
else:
  print("This file does not exist")


import os
#create a new dictionary
#os.mkdir("mydir")
#print the current working directory
print(os.getcwd())
#change the current working directory
os.chdir("mydir")
print(os.getcwd())
#delete the directory that we created
#os.rmdir("mydir")
#to go back to previous directory
#os.chdir("..")
print(os.getcwd())
#delete the directory that we created
#os.rmdir("mydir")
#os.mkdir("mydir")
#get the list of files and folders in a dir
result = os.listdir(os.getcwd())
print(result)


#A simple demostration of exception handling in python
#using the try, except, finally blocks (clause)

try:
  div = 4//2
  print(div)

except ZeroDivisionError as e:
  print("You are trying to divide a number by 0.")
  print(f"{type(e).__name__} was occured. More details below: ")
  print(e) #print entire details of the exception

else: #else will work if the try statements are successful
  print("division completed and result is",div)
finally:
  print("I will run whatever happens.")

#Nested try exceot statements in python: a scenario
try: 
  f=open("myfile.txt")
  try:
    f.write("Hello World")
  except:
    print("Some write error occured.")
  finally:
    f.close()
except:
  print("The file cannot be opened.")

#importing pyodbc module
from cmath import e
from tkinter import E
import pyodbc

#create a connection string
myConString = 'Driver={SQL Server};Server=DESKTOP-D2MSN9I\SQLEXPRESS;Database=employee_db;Trusted_Connection=yes;'
#create a connection with connection string
myconn = pyodbc.connect(myConString)
try:

#get the cursor object
  mycursor = myconn.cursor()

#using cursor, execute SQL commands
  mycursor.execute('CREATE TABLE EmployeeMaster3'
'(Id INT IDENTITY PRIMARY KEY,'
	'EmployeeCode VARCHAR(10),'
	'EmployeeName VARCHAR(25),'
	'DepartmentCode VARCHAR(10),'
	'LocationCode VARCHAR(10),'
	'Salary INT)')
except Exception as e:
  print("Cannot create the table because :")
  print(f"{type(e).__name__} has occured.")
  print(e)

myconn.commit()
myconn.close()

import pyodbc
#create a connection string
myConString = 'Driver={SQL Server};Server=DESKTOP-D2MSN9I\SQLEXPRESS;Database=employee_db;Trusted_Connection=yes;'
#create a connection with connection string
myconn = pyodbc.connect(myConString)
mycursor = myconn.cursor()
try:

#get the cursor object
  mycursor = myconn.cursor()

#using cursor, execute SQL commands
  mycursor.execute('SELECT * FROM EmployeeMaster')
except Exception as e:
  print("Cannot read the table :")
  print(e)


'''for row in mycursor.fetchall():
  print(row)'''

employees = [{'empcode':row[1],'empname':row[2]} for row in mycursor.fetchall()]
print(employees)

myconn.close()


import pyodbc
#create a connection string
myConString = 'Driver={SQL Server};Server=DESKTOP-D2MSN9I\SQLEXPRESS;Database=employee_db;Trusted_Connection=yes;'
#create a connection with connection string
myconn = pyodbc.connect(myConString)
mycursor = myconn.cursor()
try:

#get the cursor object
  mycursor = myconn.cursor()

#using cursor, execute SQL commands
  #mycursor.execute("INSERT INTO EmployeeMaster VALUES ('E0888', 'Arjun', 'IT', 'TVM', 4000)")
  #mycursor.execute('SELECT * FROM EmployeeMaster')
  mycursor.execute("INSERT INTO EmployeeMaster VALUES (?,?,?,?,?)",('E0899', 'Arjuna', 'IT', 'TVM', 9000))
except Exception as e:
  print("Cannot read the table :")
  print(e)

for row in mycursor.fetchall():
  print(row)

myconn.commit()
myconn.close()

#user raising an exception explicitly for conditions
x = 0
if x == 0:
  #using raise keyword  we can manually raise an exception
  raise Exception("The number cannot be zero")

x = "hello"
if not type(x) is int:
  raise TypeError("Int values are allowed")

  #creating a user defined Exception class
#exceptions should be derived from the built-in exception class

#creating a class inheriting the built-in Exception class
class myError(Exception):
  #constructor method
  def __init__(self, value):
    self.value = value
  #__str__ display dunder function
  def __str__(self):
    return(repr(self.value))
#__str__ magic fn is used to get the informal string that represets
#the object 

#using the class that we just created
try:
  x = 0
  if x == 0:
    raise(myError("The number cannot be zero!"))
  
except myError as error:
  print('A new exception occured: ',error.value)
print("hello")

#the exception derived class being inherited by another class
class myError(Exception):
  #base class for exceptions
  pass

class DivideByzero(myError):
  pass

try:
  x = 0
  if x == 0:
    raise(DivideByzero)
  
except DivideByzero:
  print('A new exception occured: ')

print("hello")


#magic words or dunder methods in python
#they are special methods which is already defined/built in the python
#classes. we are overloading them to use in our program.

#to view the available dunder method in a class, we can use the dir () method
#eg: int is an obj class and to view its dunder methods
print (dir(int))

#creating a class and its object is implicityinheriting 
#an object whi9ch is built into the python interpreter

class Car:
  pass

#creating object 
car = Car()
print(car)
#<__main__.Car object at 0x000001E9A8AA7D60>
#if we want to change the behaviour of the dunder repper __repr__
#we need to overide it in the class

class Car:
  #overiding the dunder repper
  def __repr__(self):
    return f"{self.__class__.__qualname__}"

car = Car()
print(car)

class Car:
 def __str__(self):
    return f"{self.__class__.__qualname__}"

car = Car()
print(car)


#math dunder method example
#creating a class called random nos which can accept two
#nos per object
class RandomNumbers:
  def __init__(self,a,b):
    self.a = a
    self.b = b
  
#create objects for our RandomNumbers class
rand_obj_a = RandomNumbers(3,5)
rand_obj_b = RandomNumbers(6,8)

#trying to add the two random number objects
print(rand_obj_a + rand_obj_b)
#TypeError: unsupported operand type(s) for +: 'RandomNumbers' and 'RandomNumbers'

#trying to override the __add__ dunder method which is
#called implicitly when we use the '+' operator


class RandomNumbers:
  def __init__(self,a,b):
    self.a = a
    self.b = b
  
  #override the __add__ dunder method
  def __add__(self,other):
    #returning the sum of two left digits and two right digits
    #converted to random number object
    return RandomNumbers(other.a + self.a, other.b + self.b)

#to represent as string using dunder repper
#overriding the dunder repr funvtion of random nos
  def __repr__(self):
    return f"{self.__class__.__qualname__} ({self.a},{self.b})"



rand_obj_a = RandomNumbers(3,5)
rand_obj_b = RandomNumbers(6,8)

print(rand_obj_a + rand_obj_b)
 """
 #demonstarting the class dunder methods
 #creating a class with an empty list of software names
 #and an empy dict of software name and version as key value pair

from re import S


class Softwares:
  names = []
  versions = {} #hold the key value pair of sw names and sw version

  #defining (overriding) the constructor
  #invoked when we create an obj abd give the names list
  #sw1 = Softwares(['ps','msword','mspaint'])
  def __init__(self,names): #getting sw names as a list
    if names: # if names is not empty
      self.names = names.copy() #create a copy of the list
      for name in names: #looping through the list
        self.versions[name] = 1 
        #initialise sw verion to 1 for all sw names
    else:
      raise Exception("Names cannot be empty")

  #overriding the str dunder for displaying the list of sws
  #will be invoked when calling print(objname)
  #sw1 = Softwares(['ps','msword','mspaint'])
  #print(sw1)
  def __str__(self):
    #loop through the dict and print the list
    s = "The list of s/w's and its versions are: \n"
    for key,value in self.versions.items():
      s += f"{key}: version: {value} \n"
    return s

  #overriding the __setitem__ dunder method
  #this will be invoked when for eg:
  #sw1['msword'] = 2
  def __setitem__(self,name,version):
    if name in self.versions:
      self.versions[name] = version
    else:
      raise Exception("S/w name does not exist.")

  #overriding the __getitem__ dunder method
  #this will be invoked when
  #prinr(sw1['msword'])
  def __getitem__(self,name):
    if name in self.versions:
      return self.versions[name]
    else:
      raise Exception("S/w name does not exist.")

  #overriding the __delitem__ dunder method
  #this will be invoked when we delete an item
  # del sw1['msword']
  def __delitem__(self,name):
    if name in self.versions:
      #delete that item from the dictionary versions
      del self.versions[name]
      #delete the item from the names list
      self.names.remove(name)
    else:
      raise Exception("S/w name does not exist.")

  #overriding the __len__ dunder method
  #this will be invoked when calling print(len(sw1))
  def __len__(self):
    return len(self.names)

  #override the __contains__ dunder method
  #this will be invoked when calling 
  # if 'msword' in sw1: if yes, will return true, else false
  def __contains__(self,name):
    if name in self.versions:
      return True
    else:
      return False



#creating the Software Class object
sw1 = Softwares(['ps','msword','mspaint'])
#print the software class object
print(sw1)
#trying to set new version for msword software name
sw1['msword'] = 2
print(sw1)
#trying to get th eversion number for msword
sw1['msword'] = 2
print(sw1['msword'])
#delete item from dictionary
del sw1['msword']
#print(sw1['msword'])

print(len(sw1))
#checking tif the given sw name is in dictionary
if 'ps' in sw1:
  print("Software exists")
else:
  print("Software does not exist")





























