import random

score = 0
high_score = 0

def play_game():
    global score, high_score
    
    attempts = 20
    score = 0
    pc_number = random.randint(1, 20)

    print("Welcome to the Number Guessing Game!")
    print(f"You have {attempts} attempts to guess the number between 1 and 20.")

    while attempts > 0:
        guess = int(input("Guess a number between 1 and 20: "))

        if guess == pc_number:
            print("Congratulations, you've guessed the correct number!")
            score = attempts
            break
        elif guess > pc_number:
            print("Too high! Try again.")
        else:
            print("Too low! Try again.")

        attempts -= 1

    if attempts == 0 and guess != pc_number:
        print(f"Sorry, you've run out of attempts. The correct number was {pc_number}.")

    print(f"Score for this round: {score}")
    high_score = max(score, high_score)
    print(f"High Score: {high_score}")

    play_again()

def play_again():
    global score
    play = input("Do you want to play again? (yes/no): ").lower()

    if play == "yes":
        score = 0
        play_game()
    else:
        print("Thank you for playing!")



play_game()
