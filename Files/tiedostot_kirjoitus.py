"""
Learning Goals:
I learn about the error handling related to processing files.
"""
def main():
    """
    This program reads input lines from the user and
    writes then into a file.
    """
    filename = input("Enter the name of the file: ")

    try:
        # To be able to write into file the value of the
        # mode parameter for open must be "w" (write).
        save_file = open(filename, mode="w")

    except OSError:
        print(f"Writing the file {filename} was not successful.")
        return

    print("Enter rows of text. Quit by entering an empty row.")
    
    index = 0
    while True:
        text_line = input()
        index += 1

        if text_line == "":
            break

        # Everything which print would normally show on the screen
        # can be directed to a file by using the named parameter
        # file and passing a stream which was opened in "w" mode
        # as its value.
        print(index ,"", file=save_file, end ="")
        print(text_line, file=save_file)

    save_file.close()

    print(f"File {filename} has been written.")



if __name__ == "__main__":
    main()
