print("Welcome to Quizz contest")
response=input(("Do you want to play?(Type yes or no) "))
if response.lower()!="yes":
    quit()
print("Let's start! ")
score=0
answer=input("The RAM is also called as ? ")
if answer.lower()=="main memory":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")
answer=input("In MS Excel ,MS stands for ? ")
if answer.lower()=="microsoft":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")
answer=input("oops stands for? ")
if answer.lower()=="object oriented programming":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")
answer=input("SQL Stands for? ")
if answer.lower()=="structured query language":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")
print("Your total score:"+str(score))
print("Your percentage :"+str((score/4)*100)+"%")
   
    
