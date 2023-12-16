# number-guessing-game
This a beginner Number Guessing Game by python 
## Overview
This Python script implements a number guessing game where the user tries to guess a randomly generated number between 1 and 20 within a limited number of attempts.

## Functions

### `play_again()`
- **Purpose:** Starts a new round of the game.
- **Functionality:**
  - Resets the score for the new round.
  - Allows the user to play the game again.
  - Asks the user if they are ready for a new round.

### `show_high_score()`
- **Purpose:** Displays the high score achieved in the game.
- **Functionality:**
  - Compares the high score of the last round with the high score of the current round.
  - Prints the maximum value as the high score.

### `play_game()`
- **Purpose:** Implements the core logic of the number guessing game.
- **Functionality:**
  - Generates a random number between 1 and 20.
  - Allows the user to make guesses and checks against the generated number.
  - Updates the score based on the remaining attempts when the correct number is guessed.
  - Prints appropriate messages for too high, too low, or correct guesses.
  - Ends the game when attempts are exhausted or the correct number is guessed.

### `welcome()`
- **Purpose:** Greets the user and starts the game.
- **Functionality:**
  - Displays a welcome message and the number of attempts available.
  - Asks the user if they want to play the game.
  - Initiates the game based on the user's response.

## Usage
1. Run the script.
2. The game will prompt the user to play or not.
3. If the user chooses to play, the game will start.
4. The user will input guesses until they guess the correct number or exhaust all attempts.
5. After each round, the user can choose to play again or exit.
6. The high score is displayed after each round.

## Game Logic
1. Generate a random number between 1 and 20.
2. Allow the user to guess the number.
3. Check the user's guess against the generated number.
4. Provide feedback on the guess (too high, too low, or correct).
5. Update the score based on the remaining attempts when the correct number is guessed.
6. End the game when attempts are exhausted or the correct number is guessed.
7. Display the score and high score after each round.

