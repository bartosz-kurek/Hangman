import random
import sys

def hangman():
    print("Let\'s play hangman!")
    word = ask_for_word()
    difficulty = difficulty_level(force_valid_input=True)
    lives = no_of_lives(difficulty)
    play(word,lives,difficulty)

def play(word,lives,difficulty):
    graphics(difficulty, lives)
    lenght = len(word)
    word_completion = "_" * lenght
    print(word_completion)
    used_letters = set()
    guessed = False
    while not guessed and lives > 0:
        user_input = valid_input()
        if user_input in used_letters:
            print(f"You\'ve already tried {user_input}!")
        elif user_input not in word:
            lives -= 1
            used_letters.add(user_input)
            print("Wrong!")
        else:
            print("Good Guess!")
            used_letters.add(user_input)
            current_word = list(word_completion)
            indices = [i for i, letter in enumerate(word) if letter == user_input]
            for index in indices:
                current_word[index] = user_input
            word_completion ="".join(current_word)
            if "_" not in word_completion:
                guessed = True
        graphics(difficulty, lives)
        print(word_completion.capitalize())        
        print(f"Used letters - {used_letters}\n")
    if guessed:
        print("Correct word! Good job!")
    else:
        print("Game Over!")
        print(f"The word you were guessing was - {word.capitalize()}")


def ask_for_word():
    text = open("Coutries_and_Capitals.txt", "rt")
    Words = text.readlines()
    text.close()
    selected_word = random.choice(Words)
    split_word = random.choice(selected_word.split(" | "))
    corrected_word = split_word.replace("\n", "")
    final_word = corrected_word.replace(" ", "")
    return final_word.lower()

def difficulty_level(force_valid_input):
        while True:
            difficulty = input("Choose difficulty: (E)asy/(M)edium/(H)ard ").lower()
            if is_valid_difficulty(difficulty):
                return difficulty
            else:
                if not force_valid_input:
                    return None
        
def is_valid_difficulty(difficulty):
    INPUTS = ('e', 'm', 'h')
    return difficulty in INPUTS

def no_of_lives(difficulty):
    if difficulty == "e":
        return 7
    elif difficulty == "m":
        return 5
    elif difficulty == "h":
        return 3
def valid_input():
    inp = input("Please provide letter: ").lower()
    if inp == "quit":
        sys.exit("Coward!")
    else:
        return inp 
def graphics(difficulty, lives):
    if difficulty == "e":
        graphics_easy(lives)
    elif difficulty =="m":
        graphics_medium(lives)
    else:
        graphics_hard(lives)


def graphics_medium(lives):
    if lives == 5:
            print("________      ")
            print("|             ")
            print("|             ")
            print("|             ")
            print("|             ")
            print("|_____________")
    elif lives == 4:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|             ")
            print("|             ")
            print("|_____________")
    elif lives == 3:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|      ")
            print("|             ")
            print("|_____________")
    elif lives == 2:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|\     ")
            print("|             ")
            print("|_____________")
    elif lives == 1:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|\     ")
            print("|     /       ")
            print("|_____________")
    elif lives == 0:    
            print("________      ")
            print("|      |      ")
            print("|      X      ")
            print("|     /|\     ")
            print("|     / \     ")
            print("|_____________")

def graphics_hard(lives):
    if lives == 3:
            print("________      ")
            print("|             ")
            print("|             ")
            print("|             ")
            print("|             ")
            print("|_____________")
    elif lives == 2:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|             ")
            print("|             ")
            print("|_____________")
    elif lives == 1:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|\     ")
            print("|             ")
            print("|_____________")
    elif lives == 0:    
            print("________      ")
            print("|      |      ")
            print("|      X      ")
            print("|     /|\     ")
            print("|     / \     ")
            print("|_____________")

def graphics_easy(lives):
    if lives == 7:
            print("________      ")
            print("|             ")
            print("|             ")
            print("|             ")
            print("|             ")
            print("|_____________")
    elif lives == 6:
            print("________      ")
            print("|      |      ")
            print("|             ")
            print("|             ")
            print("|             ")
            print("|_____________")
    elif lives == 5:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|             ")
            print("|             ")
            print("|_____________")
    elif lives == 4:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /       ")
            print("|             ")
            print("|_____________")
    elif lives == 3:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|      ")
            print("|             ")
            print("|_____________")
    elif lives == 2:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|\     ")
            print("|             ")
            print("|_____________")
    elif lives == 1:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|\     ")
            print("|     /       ")
            print("|_____________")
    elif lives == 0:
            print("________      ")
            print("|      |      ")
            print("|      X      ")
            print("|     /|\     ")
            print("|     / \     ")
            print("|_____________")

if __name__ == '__main__':
    hangman()