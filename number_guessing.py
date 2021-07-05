import random
number = random.randint(0,10)

player_name = input("please enter your name \n")

print ("Hello "+ player_name.title() + " , guess a right number")
no_of_guess = 0

while no_of_guess < 5:
    guess = int(input())
    no_of_guess += 1
    if guess < number:
        print("your guess number is too low")
    elif guess > number:
        print("your guess number is too high")
    elif guess == number:
        print(" :) you guess number is  correct")
        break
        
else :
    print(" :( you lose the game")

        
