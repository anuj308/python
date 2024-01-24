# Enter your code here. Read input from STDIN. Print output to STDOUT
a=int(input())
t=input().split(" ")
lt=len(t)
for i in range(lt):
    t[i]=int(t[i])
z=set(t)
n=int(input())
for i in range(n):
    iz=input().split(" ")
    ixs=input().split(" ")
    ltx=len(ixs)
    for i in range(ltx):
        ixs[i]=int(ixs[i])
    ix=set(ixs)
    if iz[0]=="intersection_update":
        z.intersection_update(ix)
    elif iz[0]=="update":
        z.update(ix)
    elif iz[0]=="symmetric_difference_update":
        z.symmetric_difference_update(ix)
    elif iz[0]=="difference_update":
        z.difference_update(ix)
szzz=list(z)
print(sum(szzz))    