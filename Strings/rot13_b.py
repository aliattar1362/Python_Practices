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
    text = input("")
    text_keeper = text
    while not text == "":
        text = input("")
        text_keeper += "\n" + text
        
    my_list.append(text_keeper)
    return my_list

def convert_to_upper(text):
    """
    Encrypts its parameter using ROT13 encryption technology.

    :param text: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """
    new_text = ""
    for l in text:
        new_text += l
        
    text = "" 

    for l in new_text:
        l = l.upper()
        text += l
        
    return text
    
    
def main():
    """
    This is the main fucntion
    :param text: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()
    text = convert_to_upper(msg)
    
    print("The same, shouting:")
    print(text)
    

if __name__ == "__main__":
    main()