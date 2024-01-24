
def print_rangoli(size):
    # your code goes here
    alp="abcdefghijk"
    q=(size-1)*2+1
    line = q*2 - 1 
    st=(line/2)-1
    u=0
    for i in range(q/2):
        while u>line:
            print("-"*st+alp[size-1]+"-"*st)
            st-=2
            print("-"*st+alp[size-2]+"-"+alp[size-1]+"-"+alp[size-2]+"-"*st)
            st-=2
            print("-"*st+alp[size-3]+"-"+alp[size-2]+"-"+alp[size-1]+alp[size-3]+"-"+"-"+alp[size-2]+"-"*st)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

# link complete kar na https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true