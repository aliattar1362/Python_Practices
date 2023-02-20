"""
Learning Goals:
I learn the details related to processing files.
"""

############################################################        
        
def main():

    filename = input("Enter the name of the file: ")

    try:
        file = open(filename, mode="r")

    except OSError:
        print(f"Error: opening the file '{filename}' failed!")
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
