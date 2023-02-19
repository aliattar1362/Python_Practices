"""
Learning Goals:
Get to know default values of parameters and optional 
parameters.
"""
def calculate_angle(angle_1, angle_2 = 90):
    """
    This is the fucntion to calculate the third angle of
    a triangle. The second angle is considered euqal to 
    90 degree as the initial assumption.
    :angle_1: (float)
    """
    angle_3 = 180 - angle_1 - angle_2
    return angle_3

def main():
    """
    This is the main fucntion which prints the degree of
    third angle by callin calculate_angle function.
    """
    degree_1 = 50
    degree_2 = 60
    answer = calculate_angle(degree_1, degree_2)
    print(answer)

if __name__ == "__main__":
    main()
