"""
Learning Goals:
Getting more practice in the use of the list.
"""       
import statistics

def main():
    """
    This is the main function. It asked the amount of
    numbers in the list, and then asked user to enter
    the numbers that consist the list. Then it call 
    input_to_list function to make the list.
    """
    total_range = 5
    my_list = []
    
    for counter in range(total_range):
        print(f"Enter the time for performance {counter+1}", end="")
        entered_time = float(input(": "))
        my_list.append(entered_time)
    my_list.remove(min(my_list))
    my_list.remove(max(my_list))
    ave = statistics.mean(my_list)
    
    #index = 0
    #total = 0 
    #while not index == len(my_list):
        #total += my_list[index]
        #index += 1 
    print("The official competition score is ", end='' )
    print(f"{ave:.3} seconds.")
    #print(f"{total/len(my_list):.3} seconds.")
    
if __name__ == "__main__":
    main()