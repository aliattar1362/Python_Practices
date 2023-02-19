def compare_floats(num1, num2, EPSILON):
    """
    This is the compare_floats functino to calculate the acceptable
    difference between two values by comparing it to a constant
    value (EPSILON). This function returns the truth value (Boolean) 
    a: first value (float)
    b: second value (float)
    """
    f = True # Initialize the truth value for condition
    value = abs(num1 - num2)
    if value < EPSILON:
        f = True
    else:
        f = False
    return f

def main():
    """
    This is the main functino to calculate the acceptable difference
    between two values.
    a: first value (float)
    b: second value (float)
    """
    a = -1e-7
    b = -1.1e-7
    # Global variable for constant epsilon
    EPSILON = 1e-9
    f = compare_floats(a, b, EPSILON)
    print(f)
    
main()