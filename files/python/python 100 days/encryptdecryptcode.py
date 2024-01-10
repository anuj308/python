# secret code language

# coding rule 
# if 2 letter in a word reverse it
# if minumum 3 letter appenf first charater at end and add three random charater at start and at end
import random

a=input("Enter the message: ").split(" ")
print(a)
random_char=["pam","ted","nef","bel","roc","nim","gad","eft","aba","ait","tog","hoc","dit","gad","gig","fid","ped","suq","mew","yad","taw","col","bot"]
encrypt=""
for i in a:
    if len(i)==2:
        encrypt+=i[::-1]+"1"
    elif len(i)>=3:
        x= random.randint(0, 22)
        encrypt+= random_char[x]+i[1:]+i[0]+random_char[x]+"1"
print(encrypt)

# for decoding
a=input("Enter the message to decrypt: ").split("1")
print(a)
dencrypt=""
for i in a:
    if len(i)==2:
        dencrypt+=i[::-1]+" "
    elif len(i)>=3:
        f3= i[3:]
        # print(f3)
        lenl=len(f3)
        l3=f3[0:lenl-3]
        # print(l3)
        lenm=len(l3)
        dencrypt+=l3[-1]+l3[0:lenm-1]+" "
print(dencrypt)