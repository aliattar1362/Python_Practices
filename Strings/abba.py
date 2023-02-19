"""
Learning goals:
Learning to design an algorithm related to 
processing the strings.
""" 
def count_abbas(text):
    """
    This is the abba counter fucntion
    """ 
    #print(text)
    #print(type(text))
    counter = 0
    new_text = ""
    for l in text:
        if new_text == "" and l == "a":
            new_text += l
        elif new_text == "" and l != "a":
            new_text = ""
            
        elif new_text == "a" and l == "b":
            new_text += l
        elif new_text == "a" and l == "a":
            new_text = "a"
        elif new_text == "a" and l != "b":
            new_text = ""
            
        elif new_text == "ab" and l == "b":
            new_text += l
        elif new_text == "ab" and l == "a":
            new_text = "a"
        elif new_text == "ab" and l != "b":
            new_text = ""
        
        elif new_text == "abb" and l == "a":
            new_text += l
            counter += 1
            new_text = "a"
        elif new_text == "abb" and l != "a":
            new_text = ""
    return counter
