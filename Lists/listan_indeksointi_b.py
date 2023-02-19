"""
Learning Goals:
To practice the use of indexes when going through 
the values stored in a list.
"""
def main():
    my_list = []
    print("Give 5 numbers: ")
    for numbers in range(5):
        value = int(input("Next number: "))
        my_list.append(value)
    print("The numbers you entered, in reverse order:")
    
    index = -1
    while not index == -6:
            print(my_list[index])
            index -=1
            
if __name__ == "__main__":
    main()