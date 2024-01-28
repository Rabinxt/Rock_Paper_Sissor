import random

for_cmp = ["rock" , "paper" , "sissor"]
cmp_choose = random.choice(for_cmp)

print("Write s for sissor")
print("Write p for paper")
print("Write r for rock")

player_inp = input("Enter (rock{r} , paper{p} ,sissor{s}) : ")
print(f"Computer choose {cmp_choose}")
print(f"YOu choose {player_inp}")
def function(player_inp , cmp_choose) :
  if player_inp == "s" and cmp_choose == "paper" :
      print("You won !!")
  elif player_inp = " " :
      print("empty box , Try again")
      function(player_inp , cmp_choose)
  elif player_inp == "p"  and cmp_choose == "rock" :
      print("You won!!")
  elif player_inp == "r"  and cmp_choose == "sissor":
      print("You Won!!")
  elif player_inp == cmp_choose :
      print("It's tie")
  else:
      print("You lost , Better luck next time!!")
function(player_inp , cmp_choose)
