# -*- coding: utf-8 -*-
#match is just like switch in javascript 

e =int(input("enter number: "))
match e:
    case 3:
        print("it is three yeahh")
    case 9:
        print("it nine")
    case 10:
        print("it ten")
    case _:
        #_ is for default
        print(e)