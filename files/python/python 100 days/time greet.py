import time
hrs= int(time.strftime("%H"))
mins= int(time.strftime("%M"))
sec= int(time.strftime("%S"))
print(hrs,mins,sec)
if hrs>=0 and mins>=0 and sec>=0:
    print("Good morning")
elif hrs>=12 and mins>=0 and sec>=0:
    print("Good afternoon")
elif hrs>=18 and mins>=0 and sec>=0:
    print("Good afternoon")
elif hrs>=22 and mins>=0 and sec>=0:
    print("Good Night")