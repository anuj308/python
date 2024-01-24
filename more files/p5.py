if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split(" "))
    a1=list(arr)
    r=[]
    for i in a1:
        if i in r:
            continue
        r.append(i)
    r.sort()
    print(r[-2])