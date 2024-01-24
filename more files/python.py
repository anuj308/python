import collections
n=[]
s=[]
d={}
for i in range(int(input("enter: "))):
    name = input("enter name: ")
    score = float(input("enter marks: "))
    s.append(score)
    n.append(name)
d = dict(zip(s,n))
od = collections.OrderedDict(sorted(d.items()))
for k, v in od.items(): print(v)
