
# There are numbers between 1-1000. Let's try until we find it. The computer should determine whether it is large or small based on the number entered.
# Be careful how many moves you complete the game, after finishing it compare with your friends.
import random
count=0
num= random.randint(0,10)
while True:
    guess= int(input("Enter a number: "))
    if guess== num:
        print("Congrats!You've found it.")
        count += 1
        break
    elif guess>num :
        print("Go for smaller!")
        count += 1
    else:
        print("Go for higher!")
        count += 1
print("You guessed it on the" ,"",count,".move!")
print("You Finished the Game!.")
