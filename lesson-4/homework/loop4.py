import random
while True:
    yes_ans=['Y', 'YES', 'y', 'yes', 'ok']
    attempt=1
    max_attempt=11
    comp_guess=random.randint(1,100)
    while attempt<max_attempt:
        try:
            per_guess=int(input(f"enter your {attempt} guess: "))
        except KeyError:
            print('please enter a valid number(integer)')
            continue
        if per_guess>comp_guess:
            print("Too high!")
        elif per_guess<comp_guess:
            print("Too low!")
        else:
            print("You guess it right!")
            break
        attempt=attempt+1
    if per_guess==comp_guess:
        break
    if attempt ==max_attempt and per_guess!=comp_guess:
        ans=input("You lost. Want to play again? ")
        if ans not in yes_ans:
            print("Thanks for the game")
            break
       
        
    
   