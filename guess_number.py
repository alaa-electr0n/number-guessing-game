import random 

#starting point
score = 20 
high_score= 0 


def play_again():
    global score, high_score
    start_over=input("Are You Ready For A Whole New Round 💪(Yes/No) ").lower()
    
    if start_over == "yes":
    # restart the score value 
    # keep the high score value as it is
        score = 0

        play_game ()
    else:
        print("👋👋👋")    


def show_high_score():    
    global score , high_score 
    # compare the highscore of the last round with the high score of the current round 
    # print the max value as a high score 
    high_score= max(score, high_score)
    print (f"Your High Score Is {high_score}")
    


def play_game ():
    # to update the global variable by this function
    global score , high_score

    #guess at the game start 
    # guess = 0
    attempts = 20
    score = 0 
    
    pc_number= random.randint(1, 20)

    while  attempts > 0:
        try:
            guess = int(input("Guess A Number Between 1 and 20 ... "))
            if 20 >guess and guess <0 :
                raise ValueError("Your Guess Is Out Of Our Range!")
        except ValueError:
            print("Please Enter A Valid Number Between 1 and 20🤔 ")
        if guess == pc_number:
            print ("Congrats, YOU WON 🔥")    # show score # show High Score 
            
            score += attempts
            show_high_score()
            play_again()
            break 
        
        elif guess >pc_number:
            print ("📈 Too High Expectations, Try Lower")   # score-- 
            
            
        elif guess < pc_number:
            print ("📉 Too Low Estimation, Try Higher")     #score-- 
            
            # each wrong guess decrease the score 
        attempts -=1

    if guess != pc_number and attempts == 0:
        print (f"You Lost 😥, The Secret Number is {pc_number}")    
        
        
        print(f"Your scores: {score}")
        show_high_score()


    

# greeting the user, and play the game  
def welcome ():
    global score
    print ("Welcome to the Number Guessing Game ‼")
    print (f"You Have {score} attempts, keep the most of them! 🤞")

    # ask if the user want to play 
    while True:
        try :
            start_play = input("Do You Want To Play? (Yes/No) ").lower()
            if start_play not in ["yes", "no"]:
                raise ValueError("Invalid Answer")
            break
        except ValueError:
            ("Please Answer By Yes or No!")   
    if start_play =="yes":
        play_game()
    else:
        print ("Ok , Maybe Later 👋")    


welcome()
