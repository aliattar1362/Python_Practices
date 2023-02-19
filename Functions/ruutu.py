
def print_box(width, height, mark):
    """
    This function operates the 'print_box' by inserting
    the height, width and the sign of mark to be print.
    """
    for h in range(height):
        for w in range(width):
            print(mark, end='')
        print()

def main():
    """
    This is the main functino to operate the 'print_box'
    by asking the height, width and the sign of mark from
    user.
    """
    width = int(input("Enter the width of a frame: "))
    height = int(input("Enter the height of a frame: "))
    mark = input("Enter a print mark: ")

    print()
    print_box(width, height, mark)

if __name__ == "__main__":
    main()
