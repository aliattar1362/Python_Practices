"""
Learning Goals:
To familiarize yourself with the pre-built operations 
of a list and their call notation, i.e. the functions 
and the methods that you can use to perform operations 
for a list. At the same time, to practice the use of a 
list as a function parameter and a return value.
"""
def input_to_list(number):
    """
    This function take the numbers and put them
    inside the list and finally return that lsit.
    The input of this function is the lenght of the list.
    """
    
    my_list = []
    for n in range(number):
        value = int(input(""))
        my_list.append(value)
    return my_list
        
def main():
    """
    This is the main function. It asked the amount of
    numbers in the list, and then asked user to enter
    the numbers that consist the list. Then it call 
    input_to_list function to make the list.
    """
    
    value = int(input("How many numbers do you want to "
                      "process: "))
    print(f"Enter {value} numbers:")
    my_list = input_to_list(value)
    desired_number = int(input("Enter the number to "
                      "be searched: "))
    counter = 0
    for number in my_list:
        if number == desired_number:
            counter +=1
    if counter < 1:
        print(f"{desired_number} is not among the " 
              "numbers you have entered.")
    else:
        print(f"{desired_number} shows up {counter} " 
              "times among the numbers you have entered.")         
if __name__ == "__main__":
    main()