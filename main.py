#####################################################
## Hacktoberfest 21 project
## 21-1030 - Started game
## finished start, river, age
#### TODO: finish game
#####################################################

import replit
import time
import emoji

def check_age():
  name = input("What is your name? ")
  age = int(input("What is your age? "))
  old_enough_to_play = int(4)

  print("Hello", name, "you are", age, "years old.")
  
  if age >= old_enough_to_play:
    replit.clear()
    print("ok, you're old enough to play")
    time.sleep(2)
    replit.clear()
    edge_of_forest()

  elif age < 0:
    replit.clear()
    print(emoji.emojize("Excellent! It's Hacktoberfest so zombies can play too! :jack-o-lantern:"))

    time.sleep(2)
    replit.clear()
    edge_of_forest()

  else:
    replit.clear()
    print("Try again in ", old_enough_to_play - age, 
    "years.")
    time.sleep(2)
    replit.clear()
    start_game()

def start_game():
  check_age()

def edge_of_forest():
    where_to_go = input("You are standing alone at the edge of the forest and need to keep moving.  Where do you want to go? (L/R/U/D): ").lower()

    if "l" in where_to_go:
      river()
    elif "r":
      beach()


def river():
    replit.clear()
    
    river_task = input("You've just arrived at the river.  Your task is to bring the villagers 5 fish.  What would you like to do? (1/2/3/4): ")

    if "1" in river_task:
      print("You swam with the fish and they bit you.")
      time.sleep(2)
      river()

    elif "2" in river_task:
      print("You have just caught 5 fish.  You hold them for the villagers")
      time.sleep(2)
      river()

    elif "3" in river_task:
      print("Take a long nap while the fish jump and birds chirp")
      time.sleep(2)
      river()

    elif "4" in river_task:
      print("Go back to the edge of the forest")
      time.sleep(2)
      edge_of_forest()
      
    else:
      river()
def beach():
  print("you are at the beach")

start_game()