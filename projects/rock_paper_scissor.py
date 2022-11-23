# Day 4 project: build a rock, paper, scissor game

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
import time

gameOptions = [rock, paper, scissors]

winMsg = "Optimus Prime wins :)"
loseMsg = "You win!"
drawMsg = "It's a draw :)"

playerThrows = input("Enter your choice: rock or paper or scissor ")

print("Optimus Prime is choosing ... ")
time.sleep(0.7)

computerThrows = gameOptions[random.randint(1,3) - 1]

print(computerThrows)

if playerThrows.lower() == 'rock':
    if computerThrows == rock:
        print(drawMsg)
    elif computerThrows == paper:
        print(winMsg)
    else:
        print(loseMsg)
elif playerThrows.lower() == 'paper':
    if computerThrows == rock:
        print(loseMsg)
    elif computerThrows == paper:
        print(DrawMsg)
    else:
        print(winMsg)    
else:
    if computerThrows == rock:
        print(winMsg)
    elif computerThrows == paper:
        print(loseMsg)
    else:
        print(drawMsg)
        