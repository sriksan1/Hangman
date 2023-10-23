
import random
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