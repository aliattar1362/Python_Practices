
def main():
    # Asks the user to enter the number.
    user_number = int(input("Choose a number: "))
    for n in range(1, 11):
        result = n*user_number
        print(n, '*', user_number, '=', result)
        
if __name__ == "__main__":
    main()
