def count_substring(string, sub_string):
    x = string[::-1]
    e =0
    v = len(sub_string)
    for y in string:
        if y==sub_string:
            e+=1
    return e

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)