"""
Learning Goals:
Getting to know optional and named parameters.
"""

# TODO: the definition of print_box goes here unless it goes after main.
def print_box(height, width, border_mark = '#', inner_mark = ' '):
    """
    This is the fucntion to displays marks (inner mark and border mark) 
    based on entered height and width.
    :height: (int)
    :width: (int)
    :border_mark: Initial symbol = '#' (character)
    :inner_mark: Initial symbol = ' ' (character)
    """
    print(height * border_mark)
    for i in range(width-2):
        print(border_mark, end='')
        for j in range(height-1):
            if j == height-2:
                print(border_mark, end='')
            else:
                print(inner_mark, end='')
        print()
    print(height * border_mark)
        
    

def main():
    """
    This is the fucntion to calculate the third angle of
    a triangle. The second angle is considered euqal to 
    90 degree as the initial assumption.
    :angle_1: (float)
    """
    print_box(5, 4)
    print_box(3, 8, "*")
    print_box(5, 4, "O", "o")
    print_box(inner_mark=".", border_mark="O", height=4, width=6)


# TODO: the definition of print_box could also go here, it is up to you.


if __name__ == "__main__":
    main()
