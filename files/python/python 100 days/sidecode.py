import os

files = os.listdir("python in")
i=1
for file in files:
    if file.endswith(".txt"):
        print(file)
        os.rename(f"pyhton in/{files}",f"python in/{i}.txt")
        i=i+1