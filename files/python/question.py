n=input("a:")
if n!="z":
    if n.islower():
        print(n)
    elif n.isupper():
        n=n.lower()
        print(n)
