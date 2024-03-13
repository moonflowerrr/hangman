#IMPORTS
import random
import os
import sys
import subprocess


#DEFAULT WORD LIST
easy_list = ["hello", "cookie", "mouse",  "tissue", "apple"]

med_list = ["climbing", "wedding", "pillow", "whisper", "agenda",
    "banana"]

hard_list = ["rainbow", "bridge", "technology", "brainstorm",
    "mountain"]


#VARIABLES
guess_count = 0
correct_guess = True
winner = False
wrong = 0
input_no = False
easy_ycoord = 5
med_ycoord = 6
hard_ycoord = 5




#Single player or multiplayer
player_mode = input("Single or Multi player? ")

#SINGLE PLAYER
if(player_mode.lower() == "single"):
    mode_level = input("Easy, Medium, or Hard mode? ")
    
    if(mode_level.lower() == "easy"):
        try:
            CORRECT_WORD = easy_list.pop(random.randint(0, easy_ycoord))
            easy_ycoord -= 1
        except IndexError:
            print("You have played too many times! Please refresh to start over.")
            sys.exit()
        
    elif(mode_level.lower() == "medium"):
        try:
            CORRECT_WORD = med_list.pop(random.randint(0, med_ycoord))
            med_ycoord -= 1
        except IndexError:
            print("You have played too many times! Please refresh to start over.")
            sys.exit()
            
    elif(mode_level.lower() == "hard"):
        try:
            CORRECT_WORD = hard_list.pop(random.randint(0, hard_ycoord))
            hard_ycoord -= 1
        except IndexError:
            print("You have played too many times! Please refresh to start over.")
            sys.exit()
        
        
#MULITIPLAYER        
elif(player_mode.lower() == "multi"):
    #player names
    player1_name = input("Player one, what is your name? ")
    player2_name = input("Player two, what is your name? ")
    
    print(player2_name + " look away from the screen!")
    
    #choosing word
    word_input = input(player1_name + " choose your word: ")
    #Setting up the correct word
    CORRECT_WORD = word_input
    
    #clearing the screen
    print(" ")
    print("Player 1: " + player1_name)
    print(" ")
    print("Player 2: " + player2_name)
    print(" ")
    
    

    
#FORMATTING    
word_list = list(CORRECT_WORD)
space_list = []
for space in range(len(word_list)):
    space_list.append("__")
    
    

#Alphabet display for the user(s)
alphabet1 = "abcdefghijk"
alphabet2 = "lmnopqrstuv"
alphabet3 = "wxyz"
abc_list1 = list(alphabet1)
abc_list2 = list(alphabet2)
abc_list3 = list(alphabet3)

abc_circle1 = "ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚ"
abc_circle2 = "ⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥ"
abc_circle3 = "ⓦⓧⓨⓩ"

circle_list1 = list(abc_circle1)
circle_list2 = list(abc_circle2)
circle_list3 = list(abc_circle3)



#BEGINNNING
print("------------------------------------------")
print("------------------------------------------")
print("     |   |    /\    |\   |  /⎯⎯⎯")
print("     |___|   /  \   | \  | |    __  ")
print("     |   |  /____\  |  \ | |      |")
print("     |   | /      \ |   \|  \_____|")
print("------------------------------------------")
print("------------------------------------------")
print("       |\    /|    /\    |\   |")
print("       | \  / |   /  \   | \  |")
print("       |  \/  |  /____\  |  \ |")
print("       |      | /      \ |   \|")
print("------------------------------------------")
print("------------------------------------------")
print(" ")
print("           ______")
print("          |      |")
print("          |      |")
print("                 |")
print("                 |")
print("                 |")
print("                 |")
print("         ---------------")
print(" ")
if(len(CORRECT_WORD) == 5):
    print("    " + "    ".join(space_list))
else:
    print("    ".join(space_list))
print(" ")
print("   ".join(abc_list1))
print("   ".join(abc_list2))
print("   ".join(abc_list3))
print(" ")





#USER GUESS
def user_guess():
    global guess, correct
    guess = input("Your guess: ")

    guess = guess.lower()
    correct = False

    #If there is too many letters, the user must re-input their guess
    while len(guess) > 1:
        print("Too many letters, please input only one.")
        guess = input("Your guess: ")
    
    guess_check(guess, correct)
    
    
    
#CHECK THE USER'S GUESS
def guess_check(guess, correct):    
    global wrong, guess_count
    #This for loop sorts through the user's guess list to see
    #whether or not each character is correct or wrong
    for char in range(len(word_list)):
        
        if(guess not in space_list):
            if(guess == word_list[char]):
                space_list[char] = word_list[char]
                correct = True
            elif(guess != word_list[char]):
                correct = False
                  
        if(word_list.count(guess) > 1):
            if(guess == word_list[char]):
                space_list[char] = word_list[char]
                correct = True
        elif(guess != word_list[char]):
            pass
        
     
    abc_switch(correct)
    
    if(correct == True):
        correct_guess(abc_list1, abc_list2, abc_list3)
        incorrect_guess(wrong, abc_list1, abc_list2, abc_list3)
    elif(correct == False):
        wrong += 1
        incorrect_guess(wrong, abc_list1, abc_list2, abc_list3)
        
        
    #CHECK IF WINNER
    if("__" not in space_list):
        winner = True
        if(player_mode.lower() == "single"):
            print("------------------------------------------")
            print("------------------------------------------")
            print("You win!!")  
        elif(player_mode.lower() == "multi"):
            print("------------------------------------------")
            print("------------------------------------------")
            print(player2_name + " wins!") 
        
        
        print(" ")
        print("------------------------------------------")
        
        
        play_again()
        
    
    


#THE GUESS IS RIGHT
def correct_guess(abc_list1, abc_list2, abc_list3):
    print("------------------------------------------")
    print("------------------------------------------")
    print("     |   |    /\    |\   |  /⎯⎯⎯")
    print("     |___|   /  \   | \  | |    __  ")
    print("     |   |  /____\  |  \ | |      |")
    print("     |   | /      \ |   \|  \_____|")
    print("------------------------------------------")
    print("------------------------------------------")
    print("       |\    /|    /\    |\   |")
    print("       | \  / |   /  \   | \  |")
    print("       |  \/  |  /____\  |  \ |")
    print("       |      | /      \ |   \|")
    print("------------------------------------------")
    print("------------------------------------------")
    print(" ")
    print("           ______")
    print("          |      |")
    print("          |      |")
    print("                 |")
    print("                 |")
    print("                 |")
    print("                 |")
    print("         ---------------")
    print(" ")
    if(len(CORRECT_WORD) == 5):
        print("    " + "    ".join(space_list))
    else:
        print("    ".join(space_list))
    print(" ") 
    print(" ")
    print(" ")
    print("   ".join(abc_list1))
    print("   ".join(abc_list2))
    print("   ".join(abc_list3))
    print(" ")
    print(" ")
    print(" ")
    print(" ")


#THE GUESS IS WRONG
def incorrect_guess(wrong, abc_list1, abc_list2, abc_list3):
    if(wrong == 1):
        print("------------------------------------------")
        print("------------------------------------------")
        print("     |   |    /\    |\   |  /⎯⎯⎯")
        print("     |___|   /  \   | \  | |    __  ")
        print("     |   |  /____\  |  \ | |      |")
        print("     |   | /      \ |   \|  \_____|")
        print("------------------------------------------")
        print("------------------------------------------")
        print("       |\    /|    /\    |\   |")
        print("       | \  / |   /  \   | \  |")
        print("       |  \/  |  /____\  |  \ |")
        print("       |      | /      \ |   \|")
        print("------------------------------------------")
        print("------------------------------------------")
        print(" ")
        print("           ______")
        print("          |      |")
        print("          |      |")
        print("          O      |")
        print("                 |")
        print("                 |")
        print("                 |")
        print("         ---------------")
        print(" ")
        if(len(CORRECT_WORD) == 5):
            print("    " + "    ".join(space_list))
        else:
            print("    ".join(space_list))
        print(" ") 
        print(" ")
        print(" ")
        print("   ".join(abc_list1))
        print("   ".join(abc_list2))
        print("   ".join(abc_list3))
        print(" ")
        print(" ")
        print(" ")
        print(" ")
    elif(wrong == 2):
        print("------------------------------------------")
        print("------------------------------------------")
        print("     |   |    /\    |\   |  /⎯⎯⎯")
        print("     |___|   /  \   | \  | |    __  ")
        print("     |   |  /____\  |  \ | |      |")
        print("     |   | /      \ |   \|  \_____|")
        print("------------------------------------------")
        print("------------------------------------------")
        print("       |\    /|    /\    |\   |")
        print("       | \  / |   /  \   | \  |")
        print("       |  \/  |  /____\  |  \ |")
        print("       |      | /      \ |   \|")
        print("------------------------------------------")
        print("------------------------------------------")
        print(" ")
        print("           ______")
        print("          |      |")
        print("          |      |")
        print("          O      |")
        print("          |      |")
        print("                 |")
        print("                 |")
        print("         ---------------")
        print(" ")
        if(len(CORRECT_WORD) == 5):
            print("    " + "    ".join(space_list))
        else:
            print("    ".join(space_list))
        print(" ")
        print(" ")
        print(" ")
        print("   ".join(abc_list1))
        print("   ".join(abc_list2))
        print("   ".join(abc_list3))
        print(" ")
        print(" ")
        print(" ")
        print(" ")
    elif(wrong == 3):
        print("------------------------------------------")
        print("------------------------------------------")
        print("     |   |    /\    |\   |  /⎯⎯⎯")
        print("     |___|   /  \   | \  | |    __  ")
        print("     |   |  /____\  |  \ | |      |")
        print("     |   | /      \ |   \|  \_____|")
        print("------------------------------------------")
        print("------------------------------------------")
        print("       |\    /|    /\    |\   |")
        print("       | \  / |   /  \   | \  |")
        print("       |  \/  |  /____\  |  \ |")
        print("       |      | /      \ |   \|")
        print("------------------------------------------")
        print("------------------------------------------")
        print(" ")
        print("           ______")
        print("          |      |")
        print("          |      |")
        print("          O      |")
        print("         -|      |")
        print("                 |")
        print("                 |")
        print("         ---------------")
        print(" ")
        if(len(CORRECT_WORD) == 5):
            print("    " + "    ".join(space_list))
        else:
            print("    ".join(space_list))
        print(" ") 
        print(" ")
        print(" ")
        print("   ".join(abc_list1))
        print("   ".join(abc_list2))
        print("   ".join(abc_list3))
        print(" ")
        print(" ")
        print(" ")
        print(" ")
    elif(wrong == 4):
        print("------------------------------------------")
        print("------------------------------------------")
        print("     |   |    /\    |\   |  /⎯⎯⎯")
        print("     |___|   /  \   | \  | |    __  ")
        print("     |   |  /____\  |  \ | |      |")
        print("     |   | /      \ |   \|  \_____|")
        print("------------------------------------------")
        print("------------------------------------------")
        print("       |\    /|    /\    |\   |")
        print("       | \  / |   /  \   | \  |")
        print("       |  \/  |  /____\  |  \ |")
        print("       |      | /      \ |   \|")
        print("------------------------------------------")
        print("------------------------------------------")
        print(" ")
        print("           ______")
        print("          |      |")
        print("          |      |")
        print("          O      |")
        print("         -|-     |")
        print("                 |")
        print("                 |")
        print("         ---------------")
        print(" ")
        if(len(CORRECT_WORD) == 5):
            print("    " + "    ".join(space_list))
        else:
            print("    ".join(space_list))
        print(" ") 
        print(" ")
        print(" ")
        print("   ".join(abc_list1))
        print("   ".join(abc_list2))
        print("   ".join(abc_list3))
        print(" ")
        print(" ")
        print(" ")
        print(" ")
    elif(wrong == 5):
        print("------------------------------------------")
        print("------------------------------------------")
        print("     |   |    /\    |\   |  /⎯⎯⎯")
        print("     |___|   /  \   | \  | |    __  ")
        print("     |   |  /____\  |  \ | |      |")
        print("     |   | /      \ |   \|  \_____|")
        print("------------------------------------------")
        print("------------------------------------------")
        print("       |\    /|    /\    |\   |")
        print("       | \  / |   /  \   | \  |")
        print("       |  \/  |  /____\  |  \ |")
        print("       |      | /      \ |   \|")
        print("------------------------------------------")
        print("------------------------------------------")
        print(" ")
        print("           ______")
        print("          |      |")
        print("          |      |")
        print("          O      |")
        print("         -|-     |")
        print("         /       |")
        print("                 |")
        print("         ---------------")
        print(" ")
        if(len(CORRECT_WORD) == 5):
            print("    " + "    ".join(space_list))
        else:
            print("    ".join(space_list))
        print(" ") 
        print(" ")
        print(" ")
        print("   ".join(abc_list1))
        print("   ".join(abc_list2))
        print("   ".join(abc_list3))
        print(" ")
        print(" ")
        print(" ")
        print(" ")
    elif(wrong == 6):
        print("------------------------------------------")
        print("------------------------------------------")
        print("     |   |    /\    |\   |  /⎯⎯⎯")
        print("     |___|   /  \   | \  | |    __  ")
        print("     |   |  /____\  |  \ | |      |")
        print("     |   | /      \ |   \|  \_____|")
        print("------------------------------------------")
        print("------------------------------------------")
        print("       |\    /|    /\    |\   |")
        print("       | \  / |   /  \   | \  |")
        print("       |  \/  |  /____\  |  \ |")
        print("       |      | /      \ |   \|")
        print("------------------------------------------")
        print("------------------------------------------")
        print(" ")
        print("           ______")
        print("          |      |")
        print("          |      |")
        print("          O      |")
        print("         -|-     |")
        print("         / \     |")
        print("                 |")
        print("         ---------------")
        print(" ")
        if(len(CORRECT_WORD) == 5):
            print("    " + "    ".join(space_list))
        else:
            print("    ".join(space_list))
        print(" ") 
        print(" ")
        print(" ")
        print("   ".join(abc_list1))
        print("   ".join(abc_list2))
        print("   ".join(abc_list3))
        print(" ")
        print(" ")
        print(" ")
        print(" ")
    elif(wrong >= 7):
        loser()




#CHANGE ABC DISPLAY
def abc_switch(correct):
    #These for loops display which guessed letters
    #are right or wrong
    for letter in range(len(abc_list1)):
        if(guess == abc_list1[letter]):
            if(correct == True):
                abc_list1[letter] = circle_list1[letter]
            else:
                abc_list1[letter] = "❌"
    for letter in range(len(abc_list2)):
        if(guess == abc_list2[letter]):
            if(correct == True):
                abc_list2[letter] = circle_list2[letter]
            else:
                abc_list2[letter] = "❌"
    for letter in range(len(abc_list3)):
        if(guess == abc_list3[letter]):
            if(correct == True):
                abc_list3[letter] = circle_list3[letter]
            else:
                abc_list3[letter] = "❌"
    

#Increment the number of guesses
guess_count += 1



#THE USER LOSES    
def loser():
    winner = False
   
    if(player_mode.lower() == "single"):
        print("------------------------------------------")
        print("------------------------------------------")
        print("GAME OVER!")
        print("The correct word is " + CORRECT_WORD) 
    elif(player_mode.lower() == "multi"):
        print("------------------------------------------")
        print("------------------------------------------")
        print("GAME OVER! " + player1_name + " wins!")
        print("The correct word is " + CORRECT_WORD)
    
    
    print(" ")
    print("------------------------------------------")
    
    
    play_again()
    

#PLAY THE GAME AGAIN/START OVER
def play_again():    
    play_again = input("Would you like to play again? ")
    
    while play_again != "yes" and play_again != "no":
        print("Invalid answer. Please type yes or no.")
        play_again = input("Would you like to play again? ")
    
    if(play_again.lower() == "yes"):
        subprocess.call([sys.executable, os.path.realpath(__file__)] +
        sys.argv[1:])
        sys.exit()
    elif(play_again.lower() == "no"):
        sys.exit()
        
    play_again = " "
    
    
    
    
        
def play_game():
    while True:
        user_guess()
    
play_game()