"""
Learning Goals:
Familiarizing yourself with the prebuilt operations the list contains, 
meaning the functions and methods that you can use to perform operations 
for lists. Simultaneously, practising the use of the list as a function 
parameter.
"""
def are_all_members_same(my_list):
    """
    This function take the numbers and put them
    inside the list and finally return that lsit.
    The input of this function is the lenght of the list.
    """
    #list_length = len(my_list)
    #index = 0 
    if not len(my_list) > 0:
        answer = True
        
    else:
        refrence_value = my_list[0]
        #while not index > list_length:
        for value in my_list:
            if not value == refrence_value:
                answer = False
                break
            else: 
                answer = True
                #index += 1   
    return answer
        
def main():
    """
    This is the main function. It asked the amount of
    numbers in the list, and then asked user to enter
    the numbers that consist the list. Then it call 
    input_to_list function to make the list.
    """
    
    #my_list = [42, 42, 42, 42]
    my_list = []
    list_length = len(my_list)
    
    boolean_check = are_all_members_same(my_list)
    
    if boolean_check == True and list_length == 0:
        print("list_index_out_of_range")
        
    else:
        print(boolean_check)
  
if __name__ == "__main__":
    main()