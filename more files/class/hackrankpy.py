# Enter your code here. Read input from STDIN. Print output to STDOUT 
from itertools import permutations
a=input().split(" ")
z=list(permutations(a[0],int(a[1])))
z.sort()
str=""
for i in z:
    for j in i:
        str+=j
    print(str)
    str=""