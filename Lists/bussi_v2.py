"""
Learning Goals:
Practicing the implementation of a slightly more 
complicated list program and once again reviewing 
the operations of the remainder operator.
"""     
 
def bus_table(time):
    """
    This fucntion asks the amount of
    numbers in the list, and then asked user to enter
    the numbers that consist the list. Then it call 
    input_to_list function to make the list.
    """
    my_list = [630, 1015, 1415, 1620, 1720, 2000]
    print("The next buses leave:")
    for index in range(len(my_list)):
        if my_list[index] >= time:
            if index == len(my_list)-1:
                print(my_list[index])
                print(my_list[0])
                print(my_list[1])
                break
            elif index == len(my_list)-2:
                print(my_list[index])
                print(my_list[index+1])
                print(my_list[0])
                break
            else:
                print(my_list[index])
                print(my_list[index + 1])
                print(my_list[index + 2])
                break
        elif time > my_list[5] or time < my_list[0]:
            print(my_list[0])
            print(my_list[1])
            print(my_list[2])
            break
 
                
def main():
    """
    This is the main function. It asked the amount of
    numbers in the list, and then asked user to enter
    the numbers that consist the list. Then it call 
    input_to_list function to make the list.
    """
    time = int(input("Enter the time (as an integer): "))
    bus_table(time)
    
if __name__ == "__main__":
    main()

