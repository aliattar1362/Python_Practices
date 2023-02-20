"""
Learning Goals
Also using dict for saving the amounts and to 
execute operations where information contained 
by dict is used for calculation.
"""

def main():
    my_text =""" """
    my_dict = {}
    print("Enter rows of text for word counting. ", end="")
    print("Empty row to quit.")
    input_text = None
    
    while not input_text == "" :
        input_text = input("")
        my_text += input_text + " "
    my_text = my_text.lower()
    my_text = my_text.split()
    
    for item in my_text :
        count = my_text.count(item)
        my_dict.update({item: count})

    my_dict = dict(sorted(my_dict.items()))
    for keys, value in my_dict.items() :
        print(f"{keys} : {value} times")

if __name__ == "__main__":
    main()
