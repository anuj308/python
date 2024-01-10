x=int(input("num1:"))
y=int(input("num2:"))
i=1
a=0
if x==0 or y==0:
    print("value must not be zero")
else:
    while i<=x or i<=y:
        if x%i==0 and y%i==0:
            a=i
        i=i+1
    print("gcd:",a)