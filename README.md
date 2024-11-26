# Assignment Solutions

This repository contains the solutions for the assigned problems, including video explanations for each.

## Video Explanations

- **Video 1 (First Two Problems):**(https://drive.google.com/file/d/183o23mwFunS58N-aOTKIb6uw5JnGymkL/view?usp=drivesdk)
- **Video 2 (Final Problem):** (https://drive.google.com/file/d/181sBw8e4XOmAE1acS7SQW8j5uIllt3O9/view?usp=drivesdk)

## Problem 1: "Daily Steps Tracker"
**Description:**
You have a list of the number of steps taken each day in a month. Your task is to write a program that performs the following:
- Accepts the number of steps taken each day in the month as numbers separated by spaces.
- Calculates the highest and lowest step counts.
- Calculates the average daily step count.
- Sorts the step counts in descending order.

**Approach:**
- The program will take a list of steps input as space-separated values.
- Use built-in Python functions to find the highest, lowest, and average values.
- Use the `sorted()` function to sort the list in descending order.

## Problem 2: "Library Book Borrowing Analysis"
**Description:**
You have a record of books borrowed from a library for a month. Each record includes the book title and the number of days it was borrowed. Your task is to write a program that performs the following:
- Accepts a list of borrowed books in the format: "Book Title - Days Borrowed".
- Calculates the most and least borrowed book based on the number of days.
- Calculates the average number of days books were borrowed.
- Finds the unique titles of all borrowed books.
- Sorts the books by the number of days borrowed in descending order.

**Requirements:**
- Use a dictionary to store book titles as keys and their total borrowed days as values.
- Use a set to find unique titles of books borrowed.
- Calculate the most and least borrowed book, the average borrowing time, and sort books by borrowing duration.

**Approach:**
- Create a dictionary to store the book titles and the number of days borrowed.
- Use a set to identify unique titles of borrowed books.
- Calculate the most and least borrowed books, the average borrowing time, and sort the books based on borrowing duration.

## Problem 3: "Word Scramble Game"
**Description:**
- Create a word scramble game where the program randomly scrambles a word and gives the player a set number of attempts to guess the original word.

**Requirements:**
- The program should start by selecting a random word from a predefined list of words.
- The selected word should be scrambled (characters shuffled in a random order).
- Display the scrambled word to the player and ask them to guess the original word.
- The player should have 5 attempts to guess the word correctly.
- For each incorrect guess, the player should be informed how many attempts they have left.
- If the player guesses correctly within the attempts, display a congratulatory message.
- If the player runs out of attempts, reveal the original word.
- Handle invalid input gracefully (e.g., empty input).
- Example Interaction:

**Example Word:**
- Suppose the chosen word is "apple", which the program scrambles to "pleap".

**Game Flow:**
- The program will start by selecting a word from a predefined list.
- It will scramble the word and display it.
- The user will have five attempts to guess the original word.
- After each incorrect guess, the program will inform the player of how many attempts remain.
- If the player guesses the word correctly, a success message will be displayed.
- If the player runs out of attempts, the program will display the correct word.

**Approach:**
- Create a list of predefined words and randomly select one word using random.choice().
- Scramble the word by using random.sample() to shuffle its characters.
- Display the scrambled word and prompt the user to guess the original word.
- Allow the player 5 attempts to guess the word correctly.
- After each incorrect guess, decrease the remaining attempts and inform the player of how many attempts they have left.
- If the player guesses the word correctly, congratulate them and end the game.
- If the player runs out of attempts, reveal the original word.
- Ensure that the program handles invalid input (e.g., empty guesses) by asking the player to try again.
