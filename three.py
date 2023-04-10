# variables
# numbers
# strings
# lists
# dictionary
# # tuple

# Python - Basics, 
# Math lib, 
# data types, 
# Enum, 
# Global and Local scope, 
# Formatted strings, 
# Function declaration, 
# List operations, 
# Python tuples, 
# Object, class, 
# Functions, 
# Keyword arguments,  
# Print statement
# Mutable and Immutable objects, 
# Functions, 
# Tuples, 
# Swaping, 
# Date time, 
# Conditions, 
# Ternary operators, 
# Iterable unpacking, 
# Dictionary unpacking, 
# Optional Parameters, 
# Anonymous functions
# Initializing an instance, 
# Self argument, 
# Object creation, 
# Attributes shadowing, 
# Calling decorator function, 
# Decorators, 
# Oop concept, 
# Generator approach, 
# Generator functions, 
# Comprehensions, 
# Filter, 
# Zip, 
# Map function Syntax 
# Polymorphism,
# Operator overloading, 
# Class methods, 
# Class and Static methods, 
# Multiple inheritance, 
# Accesing a base class, 
# Eliminating duplicate codes, 
# Inheritance, 
# Exceptions, 
# Handling exceptions, 
# Opening file, 
# Reading and writing to a file, 
# Data interchange format, 
# Making HTTP request, 
# Mysql installation
# Databases and categories, 
# Database interactions.
# Creating virtual env, 
# Connecting to db using python, 
# Database interaction, 
# Crud operation
# Cryotographyand tokens, 
# Token genration, 
# TDD,

#variable is a container where we can store values
#================Python================================================
#  python is an interpreted, object oriented, high level programming language
 
# x=2
# y=x+3
#  print(y)
# name="youtube"
# print(name)
# print(name+"rocks")
# name="Nandish"
# print(name[0],name[1],name[3])
# print(name[-1])
# print(name[0:2],name[1:4],name[2:])
# name="nandish"
# print(name[4])
# name[4]='r'
# print(name)=============================strings in python are immutable====================

# myname="Nandish P"
# print(len(myname))
# print("my name is :"+myname)
# print("my name:"+myname[3:4])

#==========list=================
#list is a data structure in python that is mutable Or changeble.each element or value inside the lise is called as item
# num=[2,3,4,6,8,9,10]
# names=["nandish","Madhu","deepak",'rajesh']
# data=[num,names]
# print(data)
# num.append(45)
# num.pop(1)# if we dont specify the index it will remove last element from the stack
# #num.insert(2,88)====to inset value in specific index
# del num[2:]
# print(num)
# num.extend([100,200,300,400])
# print(num)
# print(num)
# print(num[1])
#=======python inbuild functions===========
# num=[1,6,2,7,3,4,8,5]
# x=min(num)
# y=max(num)
# z=num.sort()
# print(x,y,z)
#=========convert num to binary=========
# x=bin(25)
# print(x)
# #=======convert binary to deciaml========
# y=0b11001
# print(y)
#=======convert num to octal,hex,===========
# x=oct(25)
# print(x)
# y=hex(10)
# print(y)

#======strings=====strings means series of characters
# greeting="hello world"
# print(greeting)
# print(greeting.upper())
# print(greeting.title())
# # print(greeting.lower())
# print(greeting.lstrip())

#=====Tuple======/ collectio of values but it is almost similar to list but it is immutable
# note=tuple enhance the speed of excution because iteration in tuple is faster than list
# tup=(21,32,41,51,30,39)
# x=tup[1]
# print(tup,x)

#======Dictionary======key value pair
# data={
#     1:"nandish",
#     2:"rajesh",
#     3:"Madhu"
# }
# print(data)
# print(data[1])
# print(data[2])
# print(data.get(3))

# keys=["Nandish","MAdhu","rajesh"]
# value=["python","fastapi","reactjs"]
# data=dict(zip(keys,value))
# # print(data)
# data["city"]="cta"
# print(data)
# del data['Nandish']
# print(data)
# print(data('rajesh'))

#note dictionary is a object ,it is immutable we cannot call dict using index value

#===================functions===============function is a block of code which only run when it is called
#we pass data known as parameter into a fun ,a fun can return data as a result , it can be defined using def keyword

# def greet():
#     print("hello world")
#     print("Good morning")
# greet()    

# def add(x,y):
#     y=x+y
#     print(y)
# add(10,20)    
# add(30,50)

# def sub(x,y):
#     z=x-y
#     print(z)
# sub(10,5)    
# sub(100,50)

# def add(x,y):
#     z=x+y
#     return z
# result=add(10,30)
# print(result)

# def add_sub(x,y):
#     c=x+y
#     d=x-y
#     return c,d
# result=add_sub(20,10)
# print(result)
# print(len(result))

# def mul_div(x,y):
#     a=x*y
#     b=x/y
#     return a,b
# result=mul_div(20,10)
# print(result)

# numbers=[1,2,3,4,5,6,7,8]
# even_numbers=[]
# for number in numbers:
#     print(number)
# if number%2==0:
#     even_numbers.append(number)
# # print(even_numbers)

# for num in numbers:
#     if num%2==0:
#         print(num,end=" ")

# for num in numbers:
#     if num%2!=0:
#         print(num, end=" ")


#======formatting string====/string formatting is the process of infusing the things in the string dyanamically and presenting the string
# x=10000
# print("Nandish recived a salary of :",x)
# print(f"nandish recieved a salry of:",{x})
# print(f"Nandish recied a salary of:",{x*10})
# print(f"nandish recived a salary of :",{x/2})

#====Enumarated datatypes====(it consist of key value pair)
# employee={
#     "name":"Nandish",
#     "age":24,
#     "city":"cta",
#     "mobile":7411315773,
#     "city":"blr"

# }
# print(employee)
# import enum
 
# class Days(enum.Enum):
# ​Sun = 1
# ​Mon = 2
# ​Tue = 3

# print("The enum are: ")
 
# for i in(Days) :
# ​print(i);


# print(type(employee))
# print(len(employee))
# for key in employee:
#     print(key)
# print(employee.get("name"))    
# print(employee.get('city'))
# print(employee.get("name"),employee.get("city"),employee.get("mobile"))


#========LocalScope=========
#a variable created indside a function belongs to the local scope of a function and it can be used 
#-inside of that function
# def fun():
#     x=300
#     y=x+20
#     print(x,y)
# fun()    

# def my_fun():
#     x=300
#     y=400
#     z=x+y
#     return z
# result=my_fun()
# print(result)

#note= local var can be accessed from a function within a function

# def fun():
#     x=200
#     y=x+30
#     print(y)
#     def ano_fun():
#         print(x)
#     ano_fun()
# fun()        

#====Global scope=====a var created outside the function is global it can accseed by whole document or web page

# x=300
# def add():
#     y=x+30
#     print(y)
# add()    // suppose if we use global keyword it belongs to the global scope

# def fun():
#     global x
#     x=300
#     print(x)
# fun()    
# def add_fun():
#     y=x+30
#     print(y)
# add_fun()    

#=====Keyword arguments======/ if number of arguments is unknown add a * before the parameter name
# def funargs(*args):
#     print(args)
#     print(args[1])
# list=["Nandish","MAdhu","Rajesh","Deepak","Mark"]
# funargs(*list)    

# def fun(child1,child2,child3):
#     print("youngest child is:"+child3)
# fun(child1="mark",child2="stephan",child3="joseph")    
# def fun(x,y,z,a):
#     print("values:",x)
#     print("largest even no:",a)
# fun(x=1,y=23,z=4,a=24)    

# def fun(*kids):
#     print("the yougest child is:"+kids[2])
# fun("mark","joseph","stephan")    

# def fun(*args):
#     print("friut names are:"+args)
# fun("apple","pinapple","mango","grape")  

# def fun(**kid):              //if the number of keyword arguments is unknown add ** before the parameter
#     print("firs name of kid is:"+kid["fname"])
#     print("last name of kid is:"+kid["lname"])
#     print("fname & lname is:"+kid["fname"],kid["lname"])
# fun(fname="julie",lname="joseph")      

#passing list as a parameter
# def fun(food):
#     for x in food:
#         print(x)
# friuts=["banana","orange","apple","Pineapple"]
# fun(friuts)        

#=======Loops=======a for loop is used for iterating over a sequence

# num=[1,2,3,4,5,6,7]
# for x in num:
#     print(x)

# fruits=["apple","banana","orange","mango"]
# for x in fruits:
#     print(x)
# for y in "banana":
#     print(y)

#======Break Statement======with break statement we can stop the loop before it has looped through all the items
# fruits=["apple","banana","orange","mango"]
# for x in fruits:
#     print(x)
#     if x=="banana":   #// here it will print the x value and control comes out of the loop
#         break    

# list=[11,22,33,44,55,66]
# for num in list:
#     print(num)
#     if num==44:
#         break

# fruits=["apple","banana","orange","mango"]
# for x in fruits:
#     if x=="banana": #// here control comes out of the loop before printing x value 
#         break
#     print(x)

#====continue statememt=========
#with continue statement we can stop the current iteration of the loop and continue with the next 
# fruits=["apple","banana","orange","mango"]
# for x in fruits:
#     if x=="orange":
#         continue
#     print(x)

# list=[11,22,33,44,55]
# for x in list:
#     if x==22:
#         continue
#     print(x)

#===the range function===
#the range function returns a sequence num, starting from 0 by default and increases by 1by default & ends at specific
#number
# for x in range(5):
#     print(x) 

# for x in range(4):
#     print(x)    

#it is possible specify the increment valueby adding third parameter
# for x in range(2,10,3):
#     print(x)
# for x in range(5,50,5):
#     print(x)

#===else in for loop==it wiil print a message when the loop has ended
# for x in range(5,20,3):
#     print(x)
# else:
#     print("Loop completed")    

# for x in range(5):
#     if x==3:
#         break
#     print(x)
# else:
#     print("Loop finished")

#====nested loop ===/ a nested loop is a loop inside a loop
# value=[1,2,3,4,5]
# value=[1]
# data=["id","place","edu","name","address"]
# for x in value:
#     for y in data:
#         print(x,y)

# props=["red","taste"]
# fruits=["apple","banana","orange"]
# for x in props:
#     for y in fruits:
#         print(x,y)

#=====while Loop====/python has two preimitive loop commands 1.while loop ,2. for Loop
#with while loop we can execute set of statement as long as condition is true
# i=1
# while i<6:
#     print(i)
#     i+=1

# i=1
# while i<5:
#     print(i)
#     if i==3:
#         break
#     i+=1

#i=2
# while i<10:
#     print(i)
#     if i==5:
#         continue
#     i+=2

#===class object====
#calss is a blue print that object follows & object can be considerd as instance of a class

# class Bike:
#     def __init__(self, color, frame_material):
#         self.color = color
#         self.frame_material = frame_material
# red_bike = Bike('Red', 'Carbon Fiber')    
# print(red_bike.frame_material)
# print(red_bike.color)
# print(red_bike.frame_material,red_bike.color)

# class Car:
#     def __init__(self,color,model,price):
#         self.color=color
#         self.model=model
#         self.price=price
#     def brake(self):
#         print('brake')
#         return "Brake"
#     def clutch(self):
#         print("clutch")
#         return 'clutch'
        
# new_car=Car("blue",2023,"8 laC")
# print(new_car.color)  
# print(new_car.model,new_car.price)     #//here we are accessing the props if an object 
# print(new_car.brake())      #// here we are accessing the method of an obj
# print(new_car.clutch())

# class Student:
#     def __init__(self,read, write, play):
#         self.read=read
#         self.write=write
#         self.play=play
#     def stdnt_play(self):
#         print("hokey")
#     def stdnt_write(self):
#         print("Poems")        

# student_can=student("Books","Poems","Games")    
# print(student_can.read,student_can.write,student_can.play)
# print(student_can.stdnt_play())
# print(student_can.stdnt_write())

# def customer(name,city,age):
#     return name,city,age
# customer_details=customer("Nandish","cta",25)
# print(customer_details)
# print(customer_details.get('name'))// doubt

#====inheritance===/aquiring the properties of one class to another class 
# class Person:
#     def __init__(self,fname,lname):
#         self.firstname=fname
#         self.lastname=lname
#     def print_name(self):
#         print(self.firstname,self.lastname) 
# x=Person("Nandish",'P')
# x.print_name()

# class Book:
#     def __init__(self,title,publisher,pages):
#         self.titile=title
#         self.publisher=publisher
#         self.pages=pages

# class Ebook(Book):
#     def __init__(self, title, publisher, pages,format_):
#         self.title=title
#         self.publisher=publisher
#         self.pages=pages
#         self.format_=format_
# ebk1=Ebook("python","ABC","400","pdf")
# print(ebk1.title,ebk1.publisher,ebk1.pages,ebk1.format_)  

# #=====multiple inheritance====/A class can be derived from more than one super class in python,              
# class Mammal:
#     def mammal_info(self):
#         print("Mammals can give direct birth.")

# class WingedAnimal:
#     def winged_animal_info(self):
#         print("Winged animals can flap.")

# class Bat(Mammal, WingedAnimal):
#     pass

# #create an object of Bat class
# b1 = Bat()

# b1.mammal_info()
# b1.winged_animal_info()

# class College:
#     def teacher_info(self):
#         print("good at teching")
# class Tution:
#     def student(self):
#         print("student good at learning")
# class library(College,Tution):
#     pass

# student1=library()
# student1.teacher_info()
# student1.student()                    
#===============================================================================================

#=====POlymorpinsm=========/it is defined as performing the same task or method in different way
#for integer data types + operator is used to perform arithmetic additon operation. 
# num1=1
# num2=2
# print(num1+num2)

# # similarly for string data types + operator is used to perfom concatination
# str1="Python"
# str2="Programming"
# print(str1+str2)

# #function polymorphism in python
# print(len("Programming"))
# print(len(["Pythom","Java","C"]))
# print(len({"Name":"Nandish", "Address":"Cta", "conatct":"7411315773"}))

# class polymorphism in python:
#we can use the concept of polymorphism while creating class methods
#python allows different classes to have methods with same name

# class Cat:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age
#     def info(self):
#         print(f"i am cat.My name is {self.name}.i am {self.age} years old")
#     def place(self):
#         print("Cta")

# class Dog:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def info(self):
#         print(f"i am dog.my name is {self.name}.i am {self.age}Yeras old")
        
#     def place(self):
#         print("Dvg")
    

# cat1=Cat("kitty",2.5)
# dog1=Dog("vickey",4)
# print(dog1.info())
# print(cat1.info())

# for animal in (cat1, dog1):
#     animal.info()
#     animal.place()

#========================types of polymorphism===============
#1. method overloading and method overriding
#Method overloading/ compile time polymorphism , it is defined as method with same name diff no of ags
# class MethodOverloading:
#     def add(self, a,b):
#         print(a+b)
#     def add(self, a,b,c):
#         print(a+b+c)
# a=MethodOverloading()
# #a.add(1,2)
# a.add(1,2,3)
# #error: python does not support method overloading this is because python always picks up the latest defind one

#alternate way to perform method overloading in python 

# class Overloading:
#     def add(self, x=None , y=None):
#         if x!=None and y!=None:
#             return x+y
#         elif x!= None:
#             return x
#         else:
#             return 0
# obj=Overloading()
# print("value:", obj.add())        
# print("value:", obj.add(4))
# print("value:", obj.add(10,20))

#Metod overrriding/ methods with same name and same no of args and altleast two classes are required 
#it called as run time polymorphism

# class Class1:
#     def display(self):
#         print("Hello from class 1")
# class Class2:
#     def display(self):
#         print("Hello from class 2")
# c1=Class1()
# c2=Class2()
# c1.display() 
# c2.display()           

#Abstraction/ showing only essential parts and hiding implemtation details

# from abc import ABC, abstractmethod #/// abc is a file

# class Polygon(ABC):
#     @abstractmethod
#     def noofsides(self):
#         pass
# class Triangle(Polygon):
#     def noofsides(self):
#         print("I have 3 sides")

# class Pentagon(Polygon):
#     def noofsides(self):
#         print("I have 5 sides")

# class Hexagon(Polygon):
#     def noofsides(self):
#         print("I have 6 sides")

# class Quadralateral(Polygon):
#     def noofsides(self):
#         print("I have 4 sides")

# R= Triangle()
# R.noofsides()

# K=Quadralateral()
# K.noofsides()

# R=Pentagon()
# R.noofsides()

# K=Hexagon()
# K.noofsides()


#Encapsuloation /Encapsulation can be defined as binding variables and methods under single entity

# class Students:
#     def __init__(self, name, rank, points):
#         self.name=name
#         self.rank=rank
#         self.points=points

#     #custom function
#     def fun(self):
#         print("I am " , self.name)
#         print("I got rank " , self.rank)

# str1=Students("Steve", 1, 100 )
# str1.fun()            

# str2=Students("John", 2, 200)
# str2.fun()


# ================================Comprehensions=====================================================================
#Comprehensions in Python provide us with a short and concise(gives lot of info in few words ) way to construct new
#sequences (such as lists, set, dictionary etc.) using sequences which have been
#already defined. Python supports the following 4 types of comprehensions:

# #========Types=======
        # List Comprehensions
        # Dictionary Comprehensions
        # Set Comprehensions
        # Generator Comprehensions


# ========Using List comprehensions=========

# input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]
  
# output_list = []
  
# # Using loop for constructing output list
# for var in input_list:
#     if var % 2 == 0:
#         output_list.append(var)
  
# print("Output List using for loop:", output_list)


#Suppose we want to create an output list which contains squares of all
#the numbers from 1 to 9.

# list=[]

# for num in range(1,10):
#     list.append(num**2)
# print("Output List using for loop:", list)    


#=======Dictionary Comprehensions:======

#Suppose we want to create an output dictionary which contains only the odd numbers that are present in the input

# input_list = [1, 2, 3, 4, 5, 6, 7]
  
# output_dict = {}
  
# #Using loop for constructing output dictionary

# for var in input_list:
#     if var % 2 != 0:
#         output_dict[var] = var**3
  
# print("Output Dictionary using for loop:",output_dict )


# state = ['Gujarat', 'Maharashtra', 'Rajasthan']
# capital = ['Gandhinagar', 'Mumbai', 'Jaipur']
  
# output_dict = {}
  
# # Using loop for constructing output dictionary
# for (key, value) in zip(state, capital):
#     output_dict[key] = value
  
# print("Output Dictionary using for loop:",output_dict)

#==========Set Comprehensions:=======
#A set is a collection of unique data. That is, elements of a set cannot be duplicate.

# input_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]
  
# output_set = set()
  
# # Using loop for constructing output set
# for var in input_list:
#     if var % 2 == 0:
#         output_set.add(var)
  
# print("Output Set using for loop:", output_set)

#=========Generator Comprehensions:
#Generator Comprehensions are very similar to list comprehensions.
#ne difference between them is that generator comprehensions use circular brackets whereas list comprehensions use square brackets
#The major difference between them is that generators don’t allocate memory for the whole list. 


# input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]

# output_gen = (var for var in input_list if var % 2 == 0)
  
# print("Output values using generator comprehensions:", end = ' ')
  
# for var in output_gen:
#     print(var, end = ' ')












#=========programs for interview purpose=============

#converting list to tuple=====
# month=["jan","feb","march","april", "may", "june", "july"]
# conv_tuple=tuple(month)
# print(conv_tuple)
# print(type(conv_tuple))


# x=[1,2,3,4,5,16,17,7]
# y=sorted(x)
# print(y)

#=====swappijng of two no====
# num1=10
# num2=20
# print("num before swapping: ", num1)
# print("num before swapping:",num2)

# num1=input('Enter num1 value:')
# num2=input('Enter num2 value:')

# temp=num1    #10
# num1=num2    #20
# num2=temp ##10

# print("after swapping :",num1)
# print("after swapping :",num2)

#another approach without using temp variable==========

# num1=input('Enter num1 value:')
# num2=input('Enter num2 value:')

# num1,num2=num2,num1

# print("after swapping :",num1)
# print("after swapping :",num2)


#=========check weather no is prime or not==========
# prime no means no should divided 1 or no itself

# num=5
# count=0

# if num>1:
#     for i in range(1,num+1):
#         if(num%i)==0:
#             count=count+1
#         if count ==2:
#             print("no is prime")
#         else:
#             print("no is not prime")        





