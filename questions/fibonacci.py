x=int(input("num:"))
a=0
b=1
sum=0
c=0
i=0
while i<x:
    print(c)
    b=a
    c=b
    c=b+a
    if i%2==0:
        sum+=c
    if i>x:
        break
    i+=1
print("sum:",sum)