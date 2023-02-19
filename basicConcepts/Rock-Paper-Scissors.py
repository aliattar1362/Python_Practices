"""
Learning Goals
Learning to create a somewhat more complicated if structure.
"""
# Let’s create a game of rock-paper-scissors for two players.
# In this game, both players use one letter to tell whether 
# they choose rock (R), paper (P) or scissors (S). 
# After this, the program shows the result. Paper beats rock,
# rock beats scissors and scissors beat paper.

def main():
    
    # Get the users choice for game
    player_1 = input("Player 1, enter your choice (R/P/S): ")
    player_2 = input("Player 2, enter your choice (R/P/S): ")
    
    if player_1 == 'P' and player_2 == 'S':
        print("Player 2 won!")
        
    elif player_1 == 'P' and player_2 == 'R':
        print("Player 1 won!")
        
    elif player_1 == 'P' and player_2 == 'P':
        print("It's a tie!")
        
    elif player_1 == 'R' and player_2 == 'P':
        print("Player 2 won!")
            
    elif player_1 == 'R' and player_2 == 'S':
        print("Player 1 won!")
        
    elif player_1 == 'R' and player_2 == 'R':
        print("It's a tie!")
        
    elif player_1 == 'S' and player_2 == 'R':
        print("Player 2 won!")
                
    elif player_1 == 'S' and player_2 == 'P':
        print("Player 1 won!")
            
    elif player_1 == 'S' and player_2 == 'S':
        print("It's a tie!")
    
if __name__ == "__main__":
    main()
