#POV:Imagine you are working on a virtual board game application that simulates classic board games in a digital format. As part of this application, you need to develop a feature that simulates a simple dice game to provide users with an enjoyable gaming experience.
import random

n = int(input("Greetings! Press 1 to play the Dice Game. "))

if n==1:
    print("Welcome to the Dice Game!")
    print("Click the 'Roll Dice' button to roll the dice and find out your score.")
    input("ROLL DICE")
    a = random.randint(0,6)
    b = random.randint(0,6)
    result = a+b
    
    print(f"You rolled a {a} and a {b}. Your total score is {result}.")
else:
    print("Incorrect key, try again later!")