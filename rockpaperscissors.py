from random import randint
import time

playerscore=0
computerscore=0
list=["rock","paper","scissors"]
computer=list[randint(0,2)]
player=False 
while player==False:
  player = input("rock,paper,scissors")
  if player==computer:
    print("Tie!")
  elif player == "rock":
    if computer=="paper":
      print("computer choses", computer)
      time.sleep(2)
      print("You lose!", computer, "covers", player)
      computerscore=+1
    else:
      print("computer choses", computer)
      time.sleep(2)
      print("You win!", player, "smashes", computer)
      playerscore=+1
  elif player == "paper":
    if computer == "scissors":
      print("computer choses", computer)
      time.sleep(2)
      print("You lose!", computer, "cuts", player)
      computerscore=+1
    else:
      print("computer choses", computer)
      time.sleep(2)
      print("You win!", player, "covers", computer)
      playerscore=+1
  elif player == "scissors":
    if computer == "rock":
      print("computer choses", computer)
      time.sleep(2)
      print("You lose!", computer, "smashes", player)
      computerscore=+1
    else:
      print("computer choses", computer)
      time.sleep(2)
      print("You win!", player, "cuts", computer)
      playerscore=+1
  else:
    print("That's not a valid play. Check your spelling!")

print("player",playerscore)
print("computer",computerscore)
player=False
computer=list[randint(0,2)]