a=int(input("num: "))
n=0
sum=0
if n%2==0:
    while n<a+1:
        sum+=n
        n=n+2
    print("sum: ",sum)
else:
    while n<a:
        sum+=n
        n=n+2
    print("sum: ",sum)
