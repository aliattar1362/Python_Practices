"""
Learning goals:
Getting acquainted with string structure, ie. 
how to handle the characters in a string using a 
for command and the [] operator.
"""    
def encrypt(text  = "?"):
    """
    Encrypts its parameter using ROT13 encryption technology.

    :param text: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """

    regular_chars   = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                       "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                       "w", "x", "y", "z"]

    encrypted_chars = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                       "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                       "j", "k", "l", "m"]
    index = 0
    counter_upper = 0
    #print(text)
    #print(text.isupper())
    
    if text.isupper() == True:
        counter_upper = 1
        text = text.lower() 
        
    for l in regular_chars:
        if text == l:
            #print("index if: ", index)
            text = encrypted_chars[index]
            break
        index += 1
        #print("index: ", index)
    
    if counter_upper == 1:
        text = text.upper()
        
    #print(text)    
    return text  
encrypt()


def row_encryption(text  = "Happy, happy, joy, joy!"):
    """
    Encrypts its parameter using ROT13 encryption technology.

    :param text: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """
    counter = 0
    new_text = ""
    for l in text:
        #print(l)
        new_text += l
        counter += 1
        
    #print(new_text)
    
    text = ""
    for l in new_text:
        #print(l)
        text += encrypt(l)
    #print(text)
    return text
        
row_encryption()
