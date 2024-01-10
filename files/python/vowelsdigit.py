#wap
vowels="aeiouAEIOU"
while(True):
    a=input("vowles, or -1 to quit:")
    if a=='-1':
        break
    elif (a>='a' and a<='z') or (a>='A' and a<='Z'):
        for z in vowels:
            if a==z:
                print("vowel")
                break
        else:
            print("not vowel")
    elif (a>='0' and a<='9'):
        print("wrong input")
