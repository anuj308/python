a=input("a:")
l=list(a)
str1=""
for i in l:
    if i.isalpha():
        str1+=str(i)
print(str1)