a=int(input("k:"))
i=1
x=0
y=1
sum=0
z=0
while i<a:
    print(z)
    x=y
    y=z
    z=x+y
    if i%2==0:
        sum+=z
    if z>a:
        break
    i+=1
print("sum:",sum)
    