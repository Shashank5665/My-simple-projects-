import time
import random
Name_list = ["kite", "basket", "bike", "computer", "sky", "orange", "cube", "wash", "mouse", "white", "alien", "nature", "blade", "badge", "space"]
chance = 5
global word
global letter
chance = 5

def intro():
    global name
    name = input("What is your name: ")
    print("\n")
    time.sleep(1)
    print(f'Hello {name}, Welcome to Hangman ')
    time.sleep(1)
    print("\n")
    print("The game begins in few seconds ...")
    print("\n")
    time.sleep(2)
    print("Let's  START !")
    time.sleep(1)

def Hangman():
    global word
    global Dots
    word = random.choice(Name_list)
    
    Dots = len(word)*'_'
    print("This is the word : ",Dots)
    time.sleep(1)

def inputt():
    global word
    global Dots
    global letter
    global chance
    print("\n")
    letter = input("Enter the guess letter : ")
    if len(letter) > 1:
        print("Invalid input, Try a letter, dont add spaces ")
        time.sleep(2)
        inputt()
    elif letter in word:
        index = int(word.find(letter))
        print(index)
        Dots = Dots[:index] + letter + Dots[index + 1:]
        print(Dots)
        if Dots == word:
            time.sleep(1)
            print("CONGRULATIONS, YOU HAVE GUESSED THE WORD RIGHT ! ! !")
        else:
            inputt()
    
    elif letter not in word:
        global chance
        
        if chance == 5:
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            chance -= 1
            print(chance,"chances left")
            time.sleep(1)
            inputt()

        elif chance == 4:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            chance -= 1
            print(chance,"chances left")
            time.sleep(1)
            inputt()

        elif chance == 3:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            chance -= 1
            print(chance,"chances left")
            time.sleep(1)
            inputt()

        elif chance == 2:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            chance -= 1
            print(chance,"chance left")
            time.sleep(1)
            inputt()

        elif chance == 1:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     O \n"
                  "  |    /|\  \n"
                  "  |     | \n"
                  "  |    /|\ \n"
                  "__|__\n")
            chance -= 1
            print("YOU ARE HANGED :(")
            print("\n")
            print("The word is:",word)
        

def replay():
    print("\n")
    time.sleep(1)
    yes_or_no = input("Do you want to play again ?   y = yes, n = no  : ")
    if yes_or_no == "y":
        fun()
    else:
        print("\n")
        print("Thanks for playing !")
        print("\n")
        exit()
        print("\n")

    
            




def fun():
    intro()
    Hangman()
    inputt()


fun()
replay()