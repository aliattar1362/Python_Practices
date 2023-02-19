
def main():
    # Asks the user to enter the number.
    user_number = int(input("How many numbers would"+ \
                            " you like to have? "), )
    for n in range(1, user_number+1):
        if n % 3 == 0 and n % 7 == 0:
            print('zip boing')
        elif n % 7 == 0:
            print('boing')
        elif n % 3 == 0:
            print('zip')
        else: 
            print(n)        
if __name__ == "__main__":
    main()
