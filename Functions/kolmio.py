from math import sqrt

def area(a, b, c):
    """
    This function caclulates the area of a triangle using three
    lengths (a, b , and c) of the triangle's sides. S is half of its semiperimeter.
    """
    s = (a + b + c)/2
    ar = sqrt(s*(s-a)*(s-b)*(s-c))
    return ar

def main():
    line_1 = float(input("Enter the length of the first side: "))
    line_2 = float(input("Enter the length of the second side: "))
    line_3 = float(input("Enter the length of the third side: "))
    
    triangle_area = area(line_1, line_2, line_3)
    print("The triangle's area is", format(triangle_area, '.1f'))


if __name__ == "__main__":
    main()
