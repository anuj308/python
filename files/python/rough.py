vowels="aeiouAEIOU"

while(True):
    a=input("anfo:")
    if a=='-1':
        break
    if a>='a' and a<='z' or (a>='A' and a<='Z'):
        for i in vowels:
            if a==i:
                print("vowel")
                break
        else:
            print("not vowel")