"""
Learning goals:
Learn to implement a new program by 
combining previously implemented functions.
""" 
def read_message():
    """
    This function uses a string as a parameter 
    and returns it as written, with each word 
    starting in upper case but the rest of the 
    world in lower case.
    """
    my_list = []
    text = None
    while not text == "":
        my_list.append(text)
        text = input("")

    del(my_list[0])
    return my_list 



def encrypt(text  = "?"):
    """
    This function uses a string as a parameter 
    and returns it as written, with each word 
    starting in upper case but the rest of the 
    world in lower case.
    """
    regular_chars   = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                       "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                       "w", "x", "y", "z"]

    encrypted_chars = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                       "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                       "j", "k", "l", "m"]
    counter = 0
    counter_upper = 0
    sentence = []

    while not counter == len(text):
        new_text = ""
        
        for l in text[counter]:
            index = 0
            if l.isupper() == True:
                counter_upper = 1
                l = l.lower()
            
            for r in regular_chars:
                if l == r:
                    l = encrypted_chars[index]
                    break
                index += 1
            if counter_upper == 1:
                l = l.upper()
                counter_upper = 0
            new_text += l
        sentence.append(new_text)
        counter += 1
        
    index = 0
    while not index == len(sentence):
        print(sentence[index])
        index += 1

    
    
def main():
    """
    This is the main fucntion
    :param text: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()
    print("ROT13:")
    
    encrypt(msg)

if __name__ == "__main__":
    main()  

