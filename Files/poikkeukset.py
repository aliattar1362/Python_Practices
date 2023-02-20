"""
Learning Goals:
Learning to implement a try-except-structure for 
processing errors.
"""
############################################################
def read_input(text):

    invalid_input = True
    
    # Read the input value while it is smaller than or equal to
    # zero or of a wrong type.
    while invalid_input:
        # preapere for exceptions.   
        try:
            # Read the input from the user
            value = int(input(text))
            # Flip the flag value to end the loop.
            if value >= 1:
                invalid_input = False
            
        except ValueError:
            invalid_input = True
        
    return value 
############################################################
            
def print_box(width, height, mark):
    """
    This function operates the 'print_box' by inserting
    the height, width and the sign of mark to be print.
    """
    print()
    for h in range(height):
        for w in range(width):
            print(mark, end='')
        print()
        
#def print_box(width, height, mark):
    #for x in range(height):
        #print(width * mark)
############################################################        
        
def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")

    print_box(width, height, mark)

if __name__ == "__main__":
    main()
