import random
top_of_range=input("Enter required range of numbers:")
if top_of_range.isdigit():
    top_of_range=int(top_of_range)
else:
    print("Please! Enter an integer")
    quit()
count=0
original_number=random.randint(0,top_of_range)
while True:
    count += 1
    guessed_number=input("Guess the number:")
    if guessed_number.isdigit():
        guessed_number=int(guessed_number)
    else:
        print("Please! Enter an integer")
    if guessed_number==original_number:
        print("You got it!")
        break
    elif guessed_number>original_number:
        print("You guessed above the original ")
    else:
        print("You guessed below the original")
print("You got it in ",count,"trails")
    
