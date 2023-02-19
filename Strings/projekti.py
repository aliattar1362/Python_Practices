
from math import sqrt
 
def get_input():
    """
    This function gets the input values and make a list of 
    seawater levels. After hitting 'enter' without writting any value
    the list will be complete. It means that there is no more value to be 
    enter inside the list. Then the function returns the list to main function.
    
    : my_list: float, The empty list is occupied by entered inputs.
    :return: float, the created list.
    """
    # Create the empty list
    my_list = []
    # Define the condition to either continue adding values in list 
    # or finishing it by hitting enter in keyboard.
    while True:
        value = input("") # Get the input as string format.
        if value == "":
            break # Break if this condition is fulfiled.
        else:
            value = float(value) # Change the value to float format.
            my_list.append(value) # Add the value to list.
    # Return the list. This function os called in main fucntion.       
    return my_list 
    
    
def minimum(my_list):
    """
    This function finds the minimum value inside the input list and prints
    it with proper name and format. This function will be called in main
    function.
    
    :my_list: float, list.
    :minimum: float, the value is printed in 2 decimal numbers.
    """
    # Find the minimum of the list, change the format to 2 decimal values.
    minimum = format(min(my_list), '.2f')
    # Print it with proper distance to left side text. 
    print(f"Minimum: {minimum:>8} cm")  
    
 
def maximum(my_list):
    """
    This function finds the maximum value inside the input list and prints
    it with proper name and format. This function will be called in main
    function.
    
    :my_list: float, list.
    :maximum: float, the value is printed in 2 decimal numbers.
    """
    # Find the maximum of the list, change the format to 2 decimal values.
    maximum = format(max(my_list), '.2f')
    # Print it with proper distance to left side text. 
    print(f"Maximum: {maximum:>8} cm") 
    
    
def median(my_list):
    """
    This function finds the median value inside the input list and prints
    it with proper name and format. This function will be called in main
    function.
    
    :my_list: float, list.
    :mediam: float, the value is printed in 2 decimal numbers.
    """
    # First sort the my_list
    my_list.sort()
    # Find the length of list. It is important for finding the meadian.
    length = len(my_list)
    # For condition if the length of the list is odd.
    if length % 2 == 1:
        median = my_list[length // 2]
    # For condition if the length of the list is even.
    else:
    # The index format should be int. So it is changed to proper format.
        median = (my_list[int(length/2)] + my_list[int(length/2 - 1)]) / 2
    # Find the median of the list, change the format to 2 decimal values.    
    median = format(median,'.2f')
    # Print it with proper distance to left side text. 
    print(f"Median: {median:>9} cm")
    
    
def mean(my_list):
    """
    This function finds the mean value inside the input list and prints
    it with proper name and format. Also, this function returns mean for 
    next step for calculating Standard Deviation in correlated function. 
    This function will be called in main function.
    
    :my_list: float, list.
    :mean: float, the value is printed in 2 decimal numbers and return to
    main fucntion.
    """
    # Initialize the total values of the list. 
    total = 0
    # Calculate the total values of the list.
    for value in my_list:
        total += value
    # Calculate the mean value of the list.
    mean = total / len(my_list)
    # Find the mean of the list, change the format to 2 decimal values. 
    # Print it with proper distance to left side text. 
    print(f"Mean: {format(mean,'.2f'):>11} cm")
    # Return the mean main fucntion. It is useful for calculating Deviation.
    return mean
    
def standard_deviation(my_list, mean):
    """
    This function calculates Vairance and Standard Deviation value inside 
    the input list. the function prints Standard Deviation value with 
    proper name and format. This function will be called in main function.
    
    :my_list: float, list.
    :mean: float, the value is printed in 2 decimal numbers and return to
    main fucntion.
    """
    # Initialize the total of sum of square of the list. 
    total = 0
    for value in my_list:
    # Calculate the sum of square of each value inside the list.
        sum_square = (value - mean) ** 2
    # Initialize the total of sum of square of the list.
        total += sum_square
    # Calculate the Variance   
    var = total / (len(my_list) - 1)
    # Calculate the Standard Deviation
    std_var = format(sqrt(var), '.2f')
    # Find the mean of the list, change the format to 2 decimal values. 
    # Print it with proper distance to left side text. 
    print(f"Deviation: {std_var:>2} cm")
        
        
def main():
    """
    This is the main function. It calls several fucntions. 
    First calls get_input fucntinos to make the list.
    Then calls the functinos to calculate the desired 
    statistical values.
    """
    # When the program starts it is good to 
    # show the following advice for the user:
    print("Enter seawater levels in centimeters"
          " one per line.")
    print("End by entering an empty line.")
    # Call the fucntion to create the list.
    seawater_level = get_input()
    # If the length of the list is less than 2, the following
    # Errror message is displayed.
    if len(seawater_level) < 2:
        print("Error: At least two measurements"
              " must be entered!")
    # If the length of the list is 2 or more, the following
    # functions are called to both calculate and display proepr statistical
    # values.
    else: 
        # The function to find the minimum of the list and prints it.
        minimum(seawater_level)
        # The function to find the maximum of the list and prints it.
        maximum(seawater_level)
        # The function to find the median of the list and prints it.
        median(seawater_level)
        # The function to find the mean of the list and returns it and prints it.
        ave = mean(seawater_level)
        # The function to find the deviation of the list and prints it.
        standard_deviation(seawater_level, ave)
    
if __name__ == "__main__":
    main()

