import random as r


def getchoices():
  player_choice = input("Enter your choice (rock/paper/scissors) :")
  options = ["rock", "paper", "scissors"]
  computer_choice = r.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices


def checkwin(player, computer):
  print(f"You chose {player} and computer chose {computer} ")
  if (player == computer):
    return "its a tie"
  if (player == "rock" and computer == "scissors"):
    return "Rock smashes scissors, you win!!"
  if (player == "paper" and computer == "rock"):
    return "Paper grabs rock, paper win!!"
  if (player == "scissors" and computer == "paper"):
    return "RIP paper,you win!!"
  return "Sorry , you lose :("


choices = getchoices()
result = checkwin(choices["player"], choices["computer"])
print(result)
