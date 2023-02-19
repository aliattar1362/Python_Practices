"""
Learning Goals:
I learn about the error handling related to processing files.
"""

############################################################        
        
def main():
    """
    This function reads the number entered by the user,
    checks that it is larger than zero, and returns it
    to the caller of the function.
    """
    filename = input("Enter the name of the file: ")

    try:
        file = open(filename, mode="r")

    except OSError:
        #print(f"Error: opening the file '{filename}' failed!")
        print("There was an error in reading the file.")
        return

    index = 1

    for file_line in file:
        file_line = file_line.rstrip()
 
        print(index, "", end="")
        print(file_line)
        index += 1
        
    file.close()

if __name__ == "__main__":
    main()
