
def main():
    # Defeine the boolean parameter
    r =True
    while r ==True:
        # Get the user answer.
        answer = input('Bored? (y/n) ')
        if answer == 'n':
            r =True
        elif answer == 'y':
            r =False
            print("Well, let's stop this, then.")
        else:
            print ('Incorrect entry.')
            
if __name__ == "__main__":
    main()
