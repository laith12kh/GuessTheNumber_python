import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()
logo="""
 ________  ___  ___  _______   ________   ________           _________  ___  ___  _______           ________   ___  ___  _____ ______   ________  _______   ________     
|\   ____\|\  \|\  \|\  ___ \ |\   ____\ |\   ____\         |\___   ___\\  \|\  \|\  ___ \         |\   ___  \|\  \|\  \|\   _ \  _   \|\   __  \|\  ___ \ |\   __  \    
\ \  \___|\ \  \\\  \ \   __/|\ \  \___|_\ \  \___|_        \|___ \  \_\ \  \\\  \ \   __/|        \ \  \\ \  \ \  \\\  \ \  \\\__\ \  \ \  \|\ /\ \   __/|\ \  \|\  \   
 \ \  \  __\ \  \\\  \ \  \_|/_\ \_____  \\ \_____  \            \ \  \ \ \   __  \ \  \_|/__       \ \  \\ \  \ \  \\\  \ \  \\|__| \  \ \   __  \ \  \_|/_\ \   _  _\  
  \ \  \|\  \ \  \\\  \ \  \_|\ \|____|\  \\|____|\  \            \ \  \ \ \  \ \  \ \  \_|\ \       \ \  \\ \  \ \  \\\  \ \  \    \ \  \ \  \|\  \ \  \_|\ \ \  \\  \| 
   \ \_______\ \_______\ \_______\____\_\  \ ____\_\  \            \ \__\ \ \__\ \__\ \_______\       \ \__\\ \__\ \_______\ \__\    \ \__\ \_______\ \_______\ \__\\ _\ 
    \|_______|\|_______|\|_______|\_________\\_________\            \|__|  \|__|\|__|\|_______|        \|__| \|__|\|_______|\|__|     \|__|\|_______|\|_______|\|__|\|__|
                                 \|_________\|_________|                                                                                                                 
                                                                                                                                                                         
                                                                                                                                                                         
"""
import random
random_number = random.randint(1,100)
def play():
    print(logo)
    print("I chose a number bettwen 1 to 99 try to guess it\n")
    choice = input("Choose the difficulty you want , type e to easy or h to hard : ")
    if choice == "e" :
        lives = 10
        while(lives != 0 ):
            
            guess = int(input("Type your guess here : "))
            if (guess == random_number):
                 print("You are right you guessed the number :)\n")
                 break
            elif (guess < random_number) : 
                print("Your guess is lower than the number\n Try again\n")
            else :
                print("Your guess higher than the number\n Try again\n")
            lives -=1
            print(f"You have {lives} attempts to try gurss the number\n")
    elif choice == 'h' :
        lives = 5
        while(lives != 0 ):
            
            guess = int(input("Type your guess here : "))
            if (guess == random_number):
                 print("You are right you guessed the number !!\n")
                 break
            elif (guess < random_number) : 
                print("Your guess is lower than the number\n Try again\n")
            else :
                print("Your guess higher than the number\n Try again\n")
            lives -=1
            print(f"You have {lives} attempts to try gurss the number\n")
            if(lives == 0 ) :
                print("you didnt guess the number :(")


while input("You want to play again ? type y to countinue or n to stop ") == 'y' :
    clear_screen()
    play()