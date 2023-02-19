"""
Learning Goals:
To learn about usign for loop to go through (iterate over) 
every element of a list.
"""
def main():
    my_list = []
    print("Give 5 numbers: ")
    for numbers in range(5):
        value = int(input("Next number: "))
        my_list.append(value)
    print("The numbers you entered that were greater "
          "than zero were:")
        
    for value in my_list:
       if value > 0:
            print(value)
        
if __name__ == "__main__":
    main()

