if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    i=0
    for p in scores:
        print(p)
        i+=p
    print("{0:.2f}".format(i/3))