# #assign a b ,c based upon marks obtained by student
# m=int(input("Enter marks:"))
# if m>90:
#     print("A")
# elif m>75:
#     print("B")
# elif m>60:
#     print("c")

# l=['1','2','3']
# str1=str(l)
# print(type(str1))
# print(str1)
# e=''
# for i in l:
#     e=e+i
# print(e)

d=input("data: ").split(",")
l=len(d)
for i in range(l):
    d[i]=int(d[i])
