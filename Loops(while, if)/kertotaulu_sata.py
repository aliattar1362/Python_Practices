
def main():
    # Initialize the reult of multipication: result
    result = 0
    # Initialize a repatitaion counter: c
    c = 0
    # Asks the user to enter the number.
    user_number = int(input("Choose a number: "))
    while result <= 100:
        c += 1
        result = c * user_number
        print(c, '*', user_number, '=', result)
        
if __name__ == "__main__":
    main()
