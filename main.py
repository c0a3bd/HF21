#####################################################
## Hacktoberfest 21 project
## Goal - Learn to use and configure replit change
##    control for online projects
##
## Replit - https://replit.com/
## Replit Docs - https://bit.ly/3pV67cu
#####################################################

import replit
import time

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
  edge_of_forest()

def edge_of_forest():
    where_to_go = input("You are standing alone at the edge of the forest and need to keep moving.  Where do you want to go? (L/R/U/D): ").lower()

    if "l" in where_to_go:
      river()
    elif "r":
      beach()


def river():
    replit.clear()
    
    river_task = "You've just arrived at the river.  Your task is to bring the villagers 5 fish.  What would you like to do? (1/2/3/4): "

    print(river_task)
    river_task_response = input(">")

    if "1" in river_task_response:
      print("You've caught 6 fish, but ate 3.")
      time.sleep(2)
      replit.clear()
      print(river_task)
    elif "2" in river_task_response:
      print("You have just caught 5 fish.  You hold them for the villagers")
    elif "3" in river_task_response:
      print("Take a long nap while the fish jump and birds chirp")
    elif "4" in river_task_response:
      print("Go back to the edge of the forest")
      edge_of_forest()
    else:
      replit.clear()
      print(river_task)

def beach():
  print("you are at the beach")

check_age()
