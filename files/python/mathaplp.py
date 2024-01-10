d=26
w=0
o=65
sl=[]
su=[]
num=[]
while(d>w):
    z=chr(o)
    sl.append(z.lower())
    su.append(z)
    num.append(w+1)
    w+=1
    o+=1
dl=dict(zip(sl,num))
du=dict(zip(su,num))
str1=input()
ans=""
for i in str1:
    if i.islower():
        x=dl.get(i)
    elif i.isupper():
        x=du.get(i)
    ans+=str(x)
print(ans)