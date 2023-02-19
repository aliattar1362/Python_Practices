"""
Learning Goals:
Familiarizing yourself with the prebuilt operations the 
list contains, ie. the functions and the methods that can 
be used to perform operations to the list. At the same time, 
practising the use of the list as a function parameter.
"""
def is_the_list_in_order(my_list):
    """
    This function take the numbers and put them
    inside the list and finally return that lsit.
    The input of this function is the lenght of the list.
    """
    if not len(my_list) > 0:
        answer = True
        
    else:
        refrence_value = my_list[0]
        for value in my_list:
            if value >= refrence_value:
                refrence_value = value
                answer = True
            else: 
                answer = False
                break
    return answer
        
def main():
    """
    This is the main function. It asked the amount of
    numbers in the list, and then asked user to enter
    the numbers that consist the list. Then it call 
    input_to_list function to make the list.
    """
    
    my_list = [42, 37, 43]
    #my_list = []
    list_length = len(my_list)
    
    boolean_check = is_the_list_in_order(my_list)
    
    if boolean_check == True and list_length == 0:
        print("list_index_out_of_range")
        
    else:
        print(boolean_check)
  
if __name__ == "__main__":
    main()