"""
Learning goals:
Learning to save strings in a list.
""" 
def read_message():
    """
    Encrypts its parameter using ROT13 encryption technology.

    :param text: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """
    my_list = []
    text = "None"
    while not text == "":
        text = text.upper()
        my_list.append(text)
        text = input("")
        #print(text)
    del(my_list[0])
    #print(my_list)
    return my_list 

def main():
    """
    This is the main fucntion
    :param text: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()
    #text = msg.split(",")
    #print("msg", len(msg))
    print("The same, shouting:")
    for message in msg:
        print(message)
    #print(msg)
    
if __name__ == "__main__":
    main()  
