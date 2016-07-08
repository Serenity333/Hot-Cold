from random import randint
    
    bank = randint(1,100)
    #generates the range from which a player can choose to guess from
    
    player_input = input("Please select a number from 1-100.")
    
    #heart of the game
    while number in player_input != bank:
    """This is where Python starts disliking it"""
        if player_input >= (bank + 50) or player_input >= (bank - 50):
            print("You're freezing!!!")
        elif player_input >= (bank + 25) or player_input >= (bank - 25): 
            print("You're cold.")
        elif player_input <= (bank + 10) or player_input <= (bank - 10):
            print("You're getting hot")
        elif player_input <= (bank + 5) or player_input <= (bank- 5):
            print("You're starting to catch on fire...")
        elif player_input <= (bank + 1) or player_input <= (bank - 1):
            print("You're melting!")
        elif:
            print("Are you sure you know how to play this game?")
        else player_input == bank:
            print("Congratulations! You've guessed my number!")
