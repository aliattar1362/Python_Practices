"""
Learning Goals:
Practicing the implementation of a slightly more 
complicated list program and once again reviewing 
the operations of the remainder operator.
"""     
 
def bus_table(time):

    my_list = [630, 1015, 1415, 1620, 1720, 2000]
    replace_list = []
    index = 0
    print("The next buses leave:")
    
    for data in my_list:
        if time < data :
            replace_list.append(data)
    if len(replace_list) == 0:
        while not index == 3:
            replace_list.append(my_list [index])
            index += 1
    elif len(replace_list) == 1:
        while not index == 2:
            replace_list.append(my_list [index])
            index += 1
    elif len(replace_list) == 2:
        while not index == 1:
            replace_list.append(my_list [index])
            index += 1
    print(replace_list[0])
    print(replace_list[1])
    print(replace_list[2])
 
                
def main():

    time = int(input("Enter the time (as an integer): "))
    bus_table(time)
    
if __name__ == "__main__":
    main()

