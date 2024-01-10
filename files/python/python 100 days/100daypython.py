# # f string in python
# name=input("enter name: ")
# print(f"my name is {name} ")
# print(f"in f string how to code is written {{name}} ")

# docstring and 
# docstring should be just below the function or in first line otherwise it won't  be a docstring
# def square(x):
#     '''this is a doc string in this function we take x and return the square'''
#     return x**2
# print(square(2))
# print(square.__doc__)

# import this in terminal will give zen of python a poem

# recursion 

# def factorial(n):
#     if(n==1 or n==0):
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(2))

# exception handling
# try except


# try:
#     a=int(input("enter number: "))
#     mun = [2,3,4,6,7,8,1]
#     print(mun[a])
# except IndexError:
#     print("Index error")
# except ValueError:
#     print("number enter is not integer")

# try except finally
# so finally will be executed all the time 
# we can write in print statement but in a function it wil not get executed

# def fun():
#     try:
#         n=[3,44,56,7,75,87,45,6,5]
#         a=int(input("enter index: "))
#         print(n[a])
#         return 1
#     except:
#         print("some error")
#         return 0
#     finally:
#         print("it will be executed all the time")
# print(fun())

# python error classes search on web
# raising custom error by using raise

# a=input("enter number between 5 and 9: ")

# if a=="quit":
#     pass
# elif(int(a)>5 or int(a)<9):
#     raise ValueError("number should be between 5 and 9")


# secret code language

# coding rule 
# if 2 letter in a word reverse it
# if minumum 3 letter appenf first charater at end and add three random charater at start and at end
# import random

# a=input("Enter the message: ").split(" ")
# print(a)
# random_char=["pam","ted","nef","bel","roc","nim","gad","eft","aba","ait","tog","hoc","dit","gad","gig","fid","ped","suq","mew","yad","taw","col","bot"]
# encrypt=""
# for i in a:
#     if len(i)==2:
#         encrypt+=i[::-1]+"1"
#     elif len(i)>=3:
#         x= random.randint(0, 22)
#         encrypt+= random_char[x]+i[1:]+i[0]+random_char[x]+"1"
# print(encrypt)

# # for decoding
# a=input("Enter the message to decrypt: ").split("1")
# print(a)
# dencrypt=""
# for i in a:
#     if len(i)==2:
#         dencrypt+=i[::-1]+" "
#     elif len(i)>=3:
#         f3= i[3:]
#         print(f3)
#         lenl=len(f3)
#         l3=f3[0:lenl-3]
#         print(l3)
#         lenm=len(l3)
#         dencrypt+=l3[-1]+l3[0:lenm-1]+" "
# print(dencrypt)


# short hand if else (imp)

# result= value_if_true if condition else value_if_false

# a=34
# b=3434
# print("A") if a>b else print("=") if(a==b) else print("B")

# c= 9 if b>a else 0
# print(c)
# c= 9 if a>b else 0
# print(c)

# enumerate

# virtual envirnoment in python
# link https://www.youtube.com/watch?v=nt6LlFTWOkg&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=43

# ps1 in powershell

#if __name__="__main__"

#os modules explore

# import os
# # to make folder
# os.mkdir("data")
# # to find all the folder in a folder
# os.listdir(data)

# file handling 

# reading in file
# f= open("1.py",'w')
# text=f.read()
# print(text)
# f.close()

# writing in file
# r,w,rb- read in binary, a - append mode
# f=open("2000.py",'w')
# f.write("the file is created and i am appending this string")
# f.close()

# by this method we don't have to close the file
# with open("2000.txt",'a') as f:
#     f.write("this is with i am writing")

#f.readline()
# f.write()
# f.wrtelines()

# f=open("secndtestingfiles.txt","w")
# f.write("this is a file made by f.write")
# s=[344,435,6,7,887,544,4556]
# for i in s:
#     f.write(str(i)+"\n")
#     f.writelines(str(s))
# f.close()

# with open("secndtestingfiles.txt","r") as f:
#     while True:
#         line = f.readline()
#         print(line)
#         for x in line.split(","):
#             print(x)
#         if not line:
#             break

# f.seek(10) - this allow to move the file cursor to writen position
# f.read(5)- 5 in bytes

# f.tell() - return the current position of the cursor in the file

# f.truncate()- is use to truncate the file size like
# f=open("2file.txt","w")
# f.write("in this used seek , tell, truncate ")
# f.seek(6)
# f.truncate(23)

# with open("2file.txt","r") as r:
#     data=r.read(90)
#     print(data)
#     print(r.read())
        

# # lambda function
# def apply(fuc,value):
#     return 42 + fuc(value)

# def double(x):
#     print(x*x)
# doubles = lambda x:x*2
# cube = lambda x:x**3
# avg = lambda x,y,z:x+y+z/3
# print(doubles(4))
# print(cube(4))
# print(avg(4,78,34))

# print(apply(doubles,45))
# print(apply(lambda x:x*x*x*x,45))

# map ,filter , reduce

# def cube(x):
#     return x*x*x

# lr=[2,344,56,8,94,2,4454444,76]

# # lr2=[]
# # for i in lr:
# #     lr2.append(cube(i))
# lr2=list(map(cube,lr))
# print(lr2)

# def filter_func(a):
#     return a>50
# lr3=list(filter(filter_func,lr))
# print(lr3)

# # in reduce we have to import first
# from functools import reduce
# sum = reduce(lambda x,y:x+y,lr)
# print(sum)

# different between "is" vs "=="
# both are comparition operator
# a=2
# b="2"
# print(a is b)# compare exact location of element
# print(a==b)# compre value

# oop

# self is that object which i have called
# constructors
# it is called eveytime
# self is automatically pass and in that object is passed


# class Person:
#     def __init__(self,name,occ):
#         self.name=name
#         self.occ=occ
#         print("this is called every time")
#     def info(self):
#         print(f"{self.name} is a {self.occ}")
# a=Person("Ritik","Lawyer")
# a.info()
# b=Person("Anuj","Developer")
# b.info()



# *args is to take argument in tuple,
# **kwargs is for taking argument in dict in key,value pair
# decorator (imp) day 59 cwh  watch video

# def greet(func):
#     def modi(*args, **kwargs):
#         print("Good morning")
#         func(*args, **kwargs)
#         print("thank you for using this function")
#     return modi

# @greet
# def add(x,y):
#     print(x+y)

# @greet
# def hello():
#     print("hello,....")
# add(2,4)
# hello()


# getters and setters in pythons  
# notes are imp | cwh day 60
# getter @property , setters @method_getter_name.setter
# class myclass: 
#     def __init__(self,value):
#         self.value = value
#     def show(self):
#         print(f"value is {self.value}")
    
#     @property
#     def tenx_value(self):
#         return 10*self.value
#     @tenx_value.setter
#     def tenx_value(self,new_value):
#         self.value = new_value
# pes=myclass(21)
# pes.tenx_value=85
# print(pes.tenx_value)
# pes.show()

# # inheritance in python

# class Employee:
#     def __init__(self,id,name):
#         self.id=id
#         self.name=name
#     def showdetails(self):
#         print(f"Name of Employee of {self.id} is {self.name}")
# class Programmer(Employee):
#     def showlanguage(self):
#         print(f"the core programming language is Python")

# e1=Employee(32,"Ritik")
# e2=Programmer(9,"Anuj")
# e1.showdetails()
# e2.showdetails()
# e2.showlanguage()

# access modifiers 
# public - it is by default everyone can acces it
# private - 
# protected

# # private - we can make a variable private by in start putting "__" like __name,__age , 
# # so it can't be acces directly but can be access indirectly
# # name mangling cwh notes read - 

# # print(object.__dir__()) #will give all the method that can be run by that object
# class e:
#     def __init__(self):
#         self.__name="Ritik"
# e1=e()
# print(e1.__name)#can access directly 
# print(e1._e__name)#can access indirectly by obj._classname__variable

# protected access modifiers - in naming variable we use "_" like _name,  and it can be acessed 
# so at end it is just a naming convention and only by giving "__" it will be mangled and can't be access directly and everything else is same.

# static method - can be made by @staticmethod decorator and 
# imp ---------- without self  method can be written

# class s:
#     @staticmethod
#     def add(a,b):
#         return a+b
# x=s()
# print(x.add(3,4))

# instance variable  vs class variable
# down here companyname is a class variable and self.name is an instance variable
# class employee:
#     companyname="apple"
#     noofemployee=0
#     def __init__(self,name):
#         self.name=name
#         employee.noofemployee+=1
#     def show(self):
#         print(f"{self.name} works in {self.companyname} which has {self.noofemployee} employee")
# x=employee("ritik")
# y=employee("anuj")
# print(x.companyname)
# # down both are same so 
# x.show() # in this a variable x is passing
# employee.show(x)

# x.companyname="google"
# x.show()
# y.show()

# class method - so when you have to create a method to change things for the class then
# @classmethod - just above that method so that in self instance will no go class will be passed
# but if use not used @classmethd then the name will be changed for the that instance
# class employee:
#     companyname="apple"
#     noofemployee=0
#     def __init__(self,name):
#         self.name=name
#         employee.noofemployee+=1
#     def show(self):
#         print(f"{self.name} works in {self.companyname} which has {self.noofemployee} employee")
#     @classmethod
#     def changecom(self,newcomname):
#         self.companyname=newcomname
# x=employee("ritik")
# x.show()
# x.changecom("google")
# x.show()

# class method as alternative construtor

# class employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def show(self):
#         print(f"{self.name} salary is {self.salary}")
#     # alternative constructor
#     @classmethod
#     def fromstr(cls,string):
#         return cls(string.split("-")[0],int(string.split("-")[1]))
# x=employee("ritik",70000)
# x.show()
# string="Jhon-20000"
# y=employee.fromstr(string)
# y.show()


# dir , __dict__,helf 

# print(dir(x)) will give all the method x has 
# x=[2,23,4]
# print(dir(x))

# print(x.__dict__) will give all the attribute  of x  in a dictinoary 

# class z:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# p=z("ritik",18)
# print(p.__dict__)

# # help method - is used to get help document for object,including the description of attribute nand method
# print(help(str))
# print(help(p))

# super keyword - se can call method of  parent class

# class z:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def show(self):
#         print("this is show method in parent class")
# class a(z):
#     def show(self):
#         print(f"{self.name} and age {self.age} this is show methd in child class")
#         super().show()
# p=a("ritik",18)
# p.show()


# magic/dunder method - str , repr , call 
# str - so when we print the object this method will be called 
# repr - so when we print the object this method will be called 
# call - so when we call the object this method will be called 

# class q:
#     def __init__(self,name):
#         self.name=name
#     def __call__(self):
#         return "when call  is called what "
#     def __str__(self):
#         return " when str is called or object is printed we can give the information "
#     def __repr__(self):
#         return " when repr is called or object is printed"
#     def __len__(self):
#         i=0
#         for c in self.name:
#             i+=1
#         return i
# z=q("ritik")
# print(z)
# print(str(z))
# print(repr(z))
# print(len(z))
# z()

# method overriding

# merger pdf pypdf

# operator overloading - docpython.org serach
# its not working
# class vector:
#     def __init__(self,i,j,k):
#         self.i=i
#         self.j=j
#         self.k=k
#     def __str__(self):
#         return f"{self.i}i + {self.j}j + {self.k}k"
#     def __add__(self,xt):
#         return vector(self.i + xt.i , self.j + xt.j + self.k + xt.k)
#     def __sub__(self,xt):
#         return vector(self.i - xt.i , self.j - xt.j , self.k - xt.k)

# v1=vector(2,4,6)
# print(v1)
# v2=vector(9,6,9)
# print(v2)
# print(v1 + v2)

# single , multiple inheritance 
# class.mro()
# multiple level inheritance
# hybrid, hierarchical inheritance
# hybrid - in a program multiple inheritance is used and it is 
# hierarchical inheritance in which hierarchy is maintained - google the picture

# # time module 

# import time
# # time.time()
# # time.sleep()

# print(4)
# time.sleep(2)
# print("this is printed after 2 second")

# # time.strftime()

# t = time.localtime()
# f_time=time.strftime("%Y-%m-%d %H:%M-%S",t)
# print(f_time)

# command line utilities in python - video link https://www.youtube.com/watch?v=3IAu6-pgw7I&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=86


# warlus operator 

# a=True
# print(a:=False)

# numbers = [1,2,3,4]

# while(n:=len(numbers)>0):
#     print(numbers.pop())

# foods=list()
# while True:
#     food = input("what food do you like?:")
#     if food == "quit":
#         break
    # foods.append(food)

# by warlus adopt it 

# foods=list()
# while(n:=input("what food do you like?: ")!="quit"):
#     foods.append(n)

# shulti modules
# import shutil
# import os
# for file copying
# shutil.copy('1.py','cpopy.py')
# os.remove("cpopy.py")
# # for folder copying
# shutil.copytree("python in","python 100 days")
# # for moving files 
# shutil.move("python in/mergepdf.py","mergepdf.py")
# for deleting  folder 
# shutil.rmtree("python in") 


# request modules in python go to documentation 
# bs4

# import requests 
# from bs4 import BeautifulSoup
# # get 
# url = "https://www.codewithharry.com/blogpost/django-cheatsheet/"
# r = requests.get(url)
# # print(r.text)


# soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())
# for heading in soup.find_all("h2"):
#   print(heading.text)

# #   post
# # url = "https://jsonplaceholder.typicode.com/posts"

# # data = {
# #     "title": 'harry',
# #     "body": 'bhai',
# #     "userId": 12,
# #   }
# # headers =  {
# #     'Content-type': 'application/json; charset=UTF-8',
# #   }
# # response = requests.post(url, headers=headers, json=data)

# # print(response.text)

# generators read more
# in this we generator value at that time so it save memory , time

# def my_generator():
#     for i in range(3000000):
#         yield i
# gen = my_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))

# for i in gen:
#     print(i)

# function caching 

# from functools import lru_cache
# import time

# @lru_cache(maxsize=None)
# def fx(n):
#     time.sleep(5)
#     return n*5

# print(fx(20))
# print("done for 20")
# print(fx(2))
# print("done for 2")
# print(fx(6))
# print("done for 6")

# print(fx(20))
# print("done for 20")
# print(fx(2))
# print("done for 2")
# print(fx(6))
# print("done for 6")
# print(fx(65))
# print("done for 65")

# regular expressions - read pythondocs and regexr.com
# https://regexr.com/
# import re

# pattern = r"[A-Z]+yclodne"
# text = '''Cyclone Dumazile was a strong tropical cyclone in the South-West Indian Ocean that affected Madagascar and Réunion in early March 2018. Dumazile originated from a cyclone Dyclone low-pressure area that formed near Agaléga on 27 February. It became a tropical disturbance on 2 March, and was named the next day after attaining tropical storm status. Dumazile reached its peak intensity on 5 March, with 10-minute sustained winds of 165 km/h (105 mph), 1-minute sustained winds of 205 km/h (125 mph), and a central atmospheric pressure of 945 hPa (27.91 inHg). As it tracked southeastwards, Dumazile weakened steadily over the next couple of days due to wind shear, and became a post-tropical cyclone on 7 March

# '''

# match = re.search(pattern, text)
# print(match)

# matches = re.finditer(pattern, text)
# for match in matches:
#   print(match.span()) 
#   print(text[match.span()[0]: match.span()[1]])

# asyncio - https://replit.com/@growth2032/96-Day-96-AsyncIO-in-Python

# import time
# import asyncio 
# import requests


# async def function1():
#   print("func 1") 
#   URL = "https://wallpaperaccess.in/public/uploads/preview/1920x1200-desktop-background-ultra-hd-wallpaper-wiki-desktop-wallpaper-4k-.jpg"
#   response = requests.get(URL)
#   open("instagram.ico", "wb").write(response.content)
   
#   return "Harry"
  
# async def function2():
#   print("func 2") 
#   URL = "https://p4.wallpaperbetter.com/wallpaper/490/433/199/nature-2560x1440-tree-snow-wallpaper-preview.jpg"
#   response = requests.get(URL)
#   open("instagram2.jpg", "wb").write(response.content)
  
# async def function3():
#   print("func 3")
#   URL = "https://c4.wallpaperflare.com/wallpaper/622/676/943/3d-hd-wikipedia-3d-wallpaper-preview.jpg"
#   response = requests.get(URL)
#   open("instagram3.ico", "wb").write(response.content)

# async def main():
#   # await function1()
#   # await function2()
#   # await function3()
#   # return 3
#   L = await asyncio.gather(
#         function1(),
#         function2(),
#         function3(),
#     )
#   print(L)
#   # task = asyncio.create_task(function1())
#   # # await function1()
#   # await function2()
#   # await function3()

# asyncio.run(main())


# multiheading - https://replit.com/@growth2032/97-Day-97-MultiThreading-in-Python#main.py

# import threading
# import time
# from concurrent.futures import ThreadPoolExecutor

# # Indicates some task being done
# def func(seconds):
#   print(f"Sleeping for {seconds} seconds")
#   time.sleep(seconds)
#   return seconds

# def main():
#   time1 = time.perf_counter()
#   # Normal Code
#   # func(4) 
#   # func(2)
#   # func(1)
  
  
#   # Same code using Threads
#   t1 = threading.Thread(target=func, args=[4])
#   t2 = threading.Thread(target=func, args=[2])
#   t3 = threading.Thread(target=func, args=[1])
#   t1.start()
#   t2.start()
#   t3.start()
  
#   t1.join()
#   t2.join()
#   t3.join()
#   # Calculating Time 
#   time2 = time.perf_counter()
#   print(time2 - time1)


# def poolingDemo():
#   with ThreadPoolExecutor() as executor:
#     # future1 = executor.submit(func, 3)
#     # future2 = executor.submit(func, 2)
#     # future3 = executor.submit(func, 4)
#     # print(future1.result())
#     # print(future2.result())
#     # print(future3.result())
#     l = [3, 5, 1, 2]
#     results = executor.map(func, l)
#     for result in results:
#       print(result)


# poolingDemo()


# multiprocessing

# import concurrent.futures
# import requests

# def downloadFile(url, name):
#   print(f"Started Downloading {name}")
#   response = requests.get(url)
#   open(f"files/file{name}.jpg", "wb").write(response.content)
#   print(f"Finished Downloading {name}")
 


# url = "https://picsum.photos/2000/3000"
# # pros = []
# # for i in range(50):
# #   # downloadFile(url, i)
# #   p = multiprocessing.Process(target=downloadFile, args=[url, i])
# #   p.start()
# #   pros.append(p)

# # for p in pros:
# #   p.join()

# with concurrent.futures.ProcessPoolExecutor() as executor:
#   l1 = [url for i in range(60)]
#   l2 = [i for i in range(60)]
#   results = executor.map(downloadFile, l1, l2)
#   for r in results:
#     print(r)

# now what  - https://www.youtube.com/watch?v=5Pz8WGiMJ_c&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=100
# 
# make projects 
# tinker