import numpy as np
import random
print()
print("-----------------------------------------------------------------------------------")
# --------- A simple way to understand the Random Number
print("Random number:", random.random())

random_number = random.randint(0, 1)
if (random_number):
    print("Tails")
else:
    print("Heads")
    
# -------------------------------------------------------
# --------- Lists
folclore_brasileiro = [
    "Saci-Pererê",
    "Curupira",
    "Iara",
    "Boitatá",
    "Cuca",
    "Boto-cor-de-rosa",
    "Mula-sem-cabeça",
    "Caipora",
    "Lobisomem",
    "Negrinho do Pastoreio",
    "Cabra-Cabriola",
    "Vitória-Régia"
]
print(len(folclore_brasileiro))
folclore_brasileiro.extend([
    "Matinta Perera",
    "Corpo-Seco",
    "Quibungo"
])

print("This was extended to", len(folclore_brasileiro), "characters")
print(folclore_brasileiro)

print("------ THE GAME -------")
print("I will chose two characters to play:")
current_player = random.randint(0, len(folclore_brasileiro)-1)
print("-", folclore_brasileiro[current_player])

# Tem uma forma mais doida de fazer isso. Pega!
print("-", random.choice(folclore_brasileiro))

print(folclore_brasileiro[current_player], "will play with you")

print()
print("------------------------------------------------")
# 
# Rock
rock = ("""
ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
PAPER
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors = ("""
SCISSORS
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

all_options = [rock, paper, scissors]

chosing_option = True
while chosing_option:
    your_choice = int(input("Select an option: [0] ROCK, [1] PAPER, [2] SCISSOR\n"))

    valid_options = [0, 1, 2]

    if your_choice in valid_options:
        chosing_option = False
    else:
        print("What's your problem? You have to choise a valid option!")
    
print("YOU:", your_choice,  all_options[your_choice])
computer_choice = random.randint(0, 2)

print("COMPUTER:", computer_choice,  all_options[computer_choice])

print("---------------------")
if (your_choice == 0 and computer_choice == 2) or \
    (your_choice == 1 and computer_choice == 0) or \
    (your_choice == 2 and computer_choice == 1):
        print("YOU WON!")
elif (your_choice == computer_choice):
    print("No winner...")
else:
    print("You're defeated! Ashame!...")

print("-----------------------------------------------------------------------------------")
print()