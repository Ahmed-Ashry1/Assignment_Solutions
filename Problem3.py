import random

def word_scramble_game():
    word_list = ["apple", "banana", "mango", "orange"]
    
    org_word = random.choice(word_list)
    scrambled_word = ''.join(random.sample(org_word, len(org_word)))
    
    print("Welcome to the Word Scramble Game!")
    print(f"Try to guess the original word from the scrambled word: {scrambled_word}")
    print("You have 5 attempts.")
    
    attempts = 5
    
    while attempts > 0:
        guess = input("Enter your guess: ").strip().lower()
        
        if not guess:
            print("Invalid input. Please try again.")
            continue
        
        if guess == org_word:
            print("Congratulations! You guessed the correct word!")
            return
        
        attempts -= 1
        if attempts > 0:
            print(f"Incorrect. Try again! You have {attempts} attempts left.")
        else:
            print(f"You're out of attempts. The original word was: {org_word}")

word_scramble_game()
