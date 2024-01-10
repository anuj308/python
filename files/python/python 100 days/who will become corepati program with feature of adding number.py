#who will become corepati make add your own question and answer full 
data=['question 1','answers 1','question 2','answers 2','question 3','answers 3','question 4',
      'answers 4','question 5','answers 5','question 6','answers 6']
z=0
# for adding question and answer
print("who will become corepati program make add your own question and answer ")
userinput=int(input("Enter the no of question you want to add: "))
for i in range(userinput):
    print("enter question ",i+1,"details")
    q=input("question: ")
    a=input("answer: ")
    data[i+z]=q
    data[i+z+1]=a
    z+=1
print(data)
Prize_money=0
#start the program
c=True
while c:
    p=input("enter play to play who will become corepati -")
    if(p=="play" or p=="Play"):
        print("starting....")#write rule of game what is prize at what scoree etc
        print("Rule:")
        print("1. Each right answer prize money is 1 lakh")
        print("2. For wrong answer you get nothing")
        print("3. three wrong answer in a row will disqualify you")
        noq=int(input("Enter the no of question: "))
        for i in range(noq):
            print("Question no ",i+1)
            z=0
            q=input("Enter answer: ")
            if q==data[i+1+z]:
                Prize_money+=100000
                print("correct answer and now score is ", Prize_money)
            else:        
                print("wrong answer and now score is ", Prize_money)
            z+=1
    if Prize_money>0:
        print("congratulation you have won ", Prize_money)
    else:
        print("try again next time")
    print("Money will credited to your account")
    z=input("Enter again to play again or enter exit to exit: ")
    if(z=="Exit" or z=="exit"):
        break
        
    