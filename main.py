#####################################################
## Hacktoberfest 21 project
## Goal - Learn to use and configure replit change
##    control for online projects
##
## Replit - https://replit.com/
## Replit Docs - https://bit.ly/3pV67cu
#####################################################

import replit

def check_age():
  name = input("What is your name? ")
  age = int(input("What is your age? "))
  old_enough_to_play = int(4)

  print("Hello", name, "you are", age, "years old.")
  
  if age >= old_enough_to_play:
    replit.clear()
    print("ok, you're old enough to play")
    start_game()

  elif age < 0:
    replit.clear()
    print("Excellent! It's Hacktoberfest so zombies can play too!")
    start_game()

  else:
    replit.clear()
    print("Try again in ", old_enough_to_play - age, 
    "years.")
    exit()

def start_game():
    where_to_go = input("You are standing alone and need to keep moving.  Where do you want to go? (L/R/U/D)").lower


check_age()
