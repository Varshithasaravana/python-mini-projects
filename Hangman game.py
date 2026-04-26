import random
from collections import Counter
words='''car bike bus tempo tractor train aeroplane lorry auto cycle rickshaw '''
words=words.split(" ")
word=random.choice(words)
if __name__=='__main__':
    print("Guess the word! HINT:word is a vehical")
for _ in word:
    print("_",end=" ")  #end=" " is used to print"_" in single line
    print()
    guessed_letter=''
    chances=len(word)+2
    flag=0
    try:
        while chances>0 and flag==0:
            print()
            chances-=1
            try:
                guess=input("Enter aletter to guess:").lower()
            except:
                print("Enter only a number")
                continue
            if not guess.isalpha():
                print("Enter only a number")
                continue
            elif len(guess)>1:
                print("Enter only one letter")
                continue
            elif guess in guessed_letter:
                print("You already guessed that letter")
                continue
            if guess in word:
                guessed_letter+=guess*word.count(guess)  #word.count(guess) is used to count the frequency of that lette
            for char in word:
                if char in guessed_letter:
                    print(char,end=" ")
                else:
                    print("_",end=" ")
            if Counter(guessed_letter)==Counter(word):
                print("\nCongratulations!You guessed the word:",word)
                flag=1
                break
            if chances<=0 and Counter(guessed_letter)!=Counter(word):
                print("You lost!,The word was:",word)
                break
        break
    except KeyboardInterrupt:
        print("\nGame Interrupted.Bye!")
        exit()
            


