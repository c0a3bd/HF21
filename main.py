#####################################################
## Hacktoberfest 21 project
## Goal - Learn to use and configure replit change 
##    control for online projects
## 
## Replit - https://replit.com/
## Replit Docs - https://bit.ly/3pV67cu
## Reference Tutorial - https://bit.ly/3ErPnOb
#####################################################

name = input("What is your name? ")
age = int(input("What is your age? "))

print("Hello", name, "you are", age, "years old.")

old_enough_to_play = int(4)
if age >= old_enough_to_play:
  print("ok, you're old enough to play")
elif age < 0:
    print("ok, it's Hacktoberfest so zombies can play too!")
else:
  print("come back in ", old_enough_to_play - age, "years.")
  