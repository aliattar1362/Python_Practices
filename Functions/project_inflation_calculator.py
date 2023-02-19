def main():
    # Define the 'True' indicator for 'While' condition.
    f = True
    # Initialize counter index for months.
    i = 0
    # Initialize current_number and current_difference for inflation. 
    current_number = 0 # Current inflation
    # Maximum difference between last inflation and current inflations.
    maximum_difference = 0 
    # Define While condition to do operations if f == True. 
    while f == True: 
        # Increase index of months before doing each operation.
        i +=1
        # Get the first inflation number.
        print("Enter inflation rate for month ", i, ": ", sep='', end='')
        inf_rate = input()
        # If condition to check we get a number or empty line. 
        if inf_rate: # We get the number.
            # COnver the input to a float number.
            inf_rate = float(inf_rate)
            # Calculate difference between two consecutive
            # inflations rate. 
            difference = inf_rate - current_number
            # Update the current number.
            current_number = inf_rate
            # Define difference between two consecutive inflations
            # for two first months.
            if i == 1 or i == 2:
                maximum_difference = difference  
            # Define difference between two consecutive inflations
            # (maximum inflation rate change) if for months more
            # than two.
            else:
                # Memorize the highest difference in
                # 'maximum_difference'.
                if difference >= maximum_difference:
                    maximum_difference = difference 
        else: # If we get the empty line.
            f = False
            # Display error message for conditions if we get
            # just numbers for 1 or two months. 
            if i == 1 or i == 2:
                print('Error: at least 2 monthly inflation rates '+ \
                     'must be entered.')
            # Display the final message for highest inflation
            # rate change. 
            else:
                print('Maximum inflation rate change was', \
                  format(maximum_difference, '.1f'), 'points.')
            
if __name__ == "__main__":
    main()
