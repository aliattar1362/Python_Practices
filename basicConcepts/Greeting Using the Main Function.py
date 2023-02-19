"""
Learning Goals
Learning to write a main function to a program.
"""
# Change the code of the Greetings program that asks for the
# user’s name which you have already submitted, to be
# located within a main function, which is then executed 
# using the function call.

# Define the main function.
def main():
    
    # Get the name of user
    name = input("Tell your name: ")
    # Say hello to the user
    print("Hi", name)
    print("your coding skills are great!")

if __name__ == "__main__":
    main()