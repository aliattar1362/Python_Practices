
def main():
    # Initialize to countinue the program
    coun = 'y'
    while coun == 'y':
        # Asks the user if they're bored, until they are.
        user_answer = input("Answer Y or N: ")
        if user_answer == 'y' or user_answer == 'Y' \
            or user_answer == 'n' or user_answer== 'N':
            print('You answered', user_answer)
            coun = 'n'
        else:
            print('Incorrect entry.')
            
if __name__ == "__main__":
    main()
