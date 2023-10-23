
import random
'''Step 1:
Create a function called play_game that takes word_list as a parameter. Inside the function, write the code for the following steps

Create a variable called num_lives and assign it to 5
Create an instance of the Hangman class. Do this by calling the Hangman class and assign it to a variable called game
Pass word_list and num_lives as arguments to the game object
Create a while loop and set the condition to True. In the body of the loop, do the following:
Check if the num_lives is 0. If it is, that means the game has ended and the user lost. Print a message saying 'You lost!'
Next, check if the num_letters is greater than 0. In this case, you would want to continue the game, so you need to call the ask_for_input method.
If the num_lives is not 0 and the num_letters is not greater than 0, that means the user has won the game. Print a message saying 'Congratulations. You won the game!'
Step 2:
Outside the function, call your play_game function to play your game. Don't forget to pass in your list of words as argument to the function.'''
class Hangman:
    
#Write about project here:
    """
    This is a game of Hangman. The user has to guess a word by entering a letter.
    The user has 5 lives. If the user guesses a letter that is not in the word, they lose a life.
    If the user guesses a letter that is in the word, the letter is revealed.
    The user wins if they guess all the letters in the word before they run out of lives.
    """


    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for i in range(len(self.word))]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        '''
This function checks if the user's guess is in the word.
If the guess is in the word, the letter is revealed.'''
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
        
        else:
            print(f"Sorry, {guess} is not in the word.")
            self.num_lives -= 1
            print(f"You have {self.num_lives} lives left.")
        guess = guess.lower()
        return
    def ask_for_input(self):
        '''
        This function asks the user for a letter.'''
        while True:
            guess = input("Guess a letter: ")
            if guess.isalpha() and len(guess) == 1:
                break
            else:
                print("Invalid letter. Please, enter a single alphabetical character.")
        self.check_guess(guess)
        self.list_of_guesses.append(guess)

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break
play_game(['apple', 'banana', 'orange', 'grape', 'strawberry'])
