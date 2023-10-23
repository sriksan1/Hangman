# Step 1
word = 'banana'
while True:
    # Step 2
    guess = input("Guess a letter: ")
    # Step 3
    if guess.isalpha() and len(guess) == 1:
        
        break
    
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")


# Step 1
if guess in word:
    # Step 2
    print(f"Good guess! {guess} is in the word.")
# Step 3
else:
    print(f"Sorry, {guess} is not in the word. Try again.")

def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    while True:
        guess = input("Guess a letter: ")
        if guess.isalpha() and len(guess) == 1:
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)

ask_for_input()