
def main():
    # Initialize to countinue the program
    coun = 'y'
    while coun == 'y':
        # Asks the user if they're bored, until they are.
        user_answer = input("Bored? (y/n) ")
        if user_answer == 'y':
            print('Well, let\'s stop this, then.')
            coun = 'n'
    
if __name__ == "__main__":
    main()
