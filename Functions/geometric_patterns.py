"""
Learning goals
Learning to find program parts that can be turned to functions. 
Rehearsing the creation of functions. Design your program using 
at least seven functions you defined by you. The main function does 
not count as one of them.

"""
import math

def square_func():
    """
    This function calculates and returns the circumference and 
    surface area of deired square based on its lenght.
    :lenght: input (float)
    """
    # Initialize the value for lenght
    lenght = 0
    while not lenght > 0 :
        lenght = float(input("Enter the length of the square's side: "))
    
    circumference = 4 * lenght
    surface_area = lenght **2
    
    return circumference, surface_area
    
def rectangle_func():
    """
    This function calculates and returns the circumference and 
    surface area of deired rectangle based on its lenghts.
    :lenght_1: input (float)
    :lenght_2: input (float)
    """
    # Initialize the value for lenght_1 and lenght_2
    lenght_1 = 0
    lenght_2 = 0
    
    while not lenght_1 > 0 :
        lenght_1 = float(input("Enter the length of the rectangle's side 1: "))
    while not lenght_2 > 0 :
        lenght_2 = float(input("Enter the length of the rectangle's side 2: "))
        
    circumference = (lenght_1 + lenght_2) * 2
    surface_area = lenght_1 * lenght_2
    
    return circumference, surface_area    

def circle_func():
    """
    This function calculates and returns the circumference and 
    surface area of deired circle based on its entered radius.
    :r: input radius (float)
    """
    # Initialize the value for radius
    radius = 0
    
    while not radius > 0 :
        radius = float(input("Enter the circle's radius: ")) 
    circumference = 2 * math.pi * radius
    surface_area = math.pi * (radius ** 2)
    
    return circumference, surface_area 

def print_circum_func(number):
    """
    This functinos displays the text and the value regarding the 
    circumference of correlated geometry.
    """
    print("The circumference is", format(number, '.2f'))
    
def print_surface_area_func(number):
    """
    This functinos displays the text and the value regarding the surface
    area of correlated geometry.
    """
    print("The surface area is", format(number, '.2f'))

    

def menu():
    """
    Print a menu for user to select which geometric pattern 
    to use in calculations.
    """
    while True:
        answer = input("Enter the pattern's first letter or (q)uit: ")
        
        if answer == "s":
            circumference, surface_area =  square_func()
            print_circum_func(circumference)
            print_surface_area_func(surface_area)

        elif answer == "r":
            circumference, surface_area =  rectangle_func()
            print_circum_func(circumference)
            print_surface_area_func(surface_area)
            
        elif answer == "c":
            circumference, surface_area =  circle_func()
            print_circum_func(circumference)
            print_surface_area_func(surface_area)

        elif answer == "q":
            return False

        else:
            print("Incorrect entry, try again!")

        # Empty row for the sake of readability.
        print()
        
def goodbye_func():
    """
    This function displays 'Goodbye!' to users before program be finnished.
    """
    print("Goodbye!")
    

def main():
    """
    This is the main fucntion which calls the menu function and 
    goodbye fucntion.
    """
    menu()
    goodbye_func()

if __name__ == "__main__":
    main()
