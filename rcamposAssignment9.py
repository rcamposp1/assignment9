import random

# function to flip a coin
def flip_coin():
    # dictionary to map 1 and 0 to heads and tails
    flip_dict = {1 : "heads",
    0 : "tails"}
    
    # flipping the coin
    coin_toss = flip_dict[random.randint(0,1)]
    
    # returning the coin flip result
    return coin_toss # FIXME: ADDED UNDERSCORE BETWEEN coin AND toss

# function to guess the result of 1 coin flip
def guess_coin_flip():
  
    # ask for the users guess
    user_guess = input("heads or tails? ")
  
    # flip the coin
    coin_flip = flip_coin() # FIXME: ADDED THE ASSIGNMENT OPERATOR HERE
  
    # if the users guess is correct
    if user_guess == coin_flip: # FIXME: USING == INSTEAD OF = FOR COMPARING
        print(f"correct! you guessed {user_guess} and the coin landed on {coin_flip}") # FIXME: RENAME user_guesss TO user_guess
        correct_guess = True
    
    # if the users guess is not correct
    elif user_guess != coin_flip:
        print(f"incorrect... you guessed {user_guess} and the coin landed on {coin_flip}")
        correct_guess = False
    
    # return True of False based on the result
    return correct_guess # FIXME: ADDED UNDERSCORE BETWEEN correct AND guess

# function to attempt to guess 2 consecutive correct coin flips
def guess_two_coin_flips():
  
    # counters for how many total guesses and how many consecutive successful guesses
    guess_number = 0
    successful_guesses = 0
    
    # while successful guesses is 0 or 1, guess and flip the coin
    while successful_guesses < 2:
    
        result = guess_coin_flip()
    
        # if the guess matches the coin flip
        if result == True:
            guess_number += 1
            successful_guesses += 1 # FIXME: ADDING + 1 HERE AND NOT ASSIGNING 1
        
        # if the guess does not match the coin flip
        elif result == False:
            guess_number += 1
            successful_guesses = 0
    
    print(f"2 successful guesses in a row! It took you {guess_number} guesses")
  
guess_two_coin_flips()
