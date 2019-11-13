#guess winner number between 1 to 20
import random
print("Hint Number is between 1  to 20")
winnerNum = random.randint(2,19)
print(winnerNum)
guesschance =0
a=True
while(guesschance<5):
    guesschance = 1 + guesschance
    guessNum =int(input("Enter any number to win"))
    if guessNum < winnerNum:
      print("Your number is smaller. No of Chances left "+ str(5-guesschance))
    elif guessNum> winnerNum:
        print("Your number is greater. No of Chances left " + str(5 - guesschance))
    elif guessNum==winnerNum:
     print("You won")
     print(f"Your winner number is {guessNum}")
     break
    print(f"{guessNum} is not a winner number")
    if guesschance==5:

        print("game over")
        print("do you want to play again y or n")
        restart=input("")
        if restart=="y":
            guesschance=0
        else:(print("bye bye"))
print(f"Total number of guesses you took = {guesschance}")
