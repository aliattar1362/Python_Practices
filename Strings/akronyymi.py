"""
Learning goals:
Familiarizing yourself with the string methods of Python.
"""    
def create_an_acronym(text = "central intelligence agency"):
    """
    This function requests a name as a 
    parameter and returns its acronym.
    """
    text = text.split(" ")
    #print("text:", text)
    count = 0
    keeper = ""
    #print("len(text):", len(text))
    #print(text[0]([0]) )
    while not count == len(text):
            acronym = text[count]
            keeper += acronym[0]
            count += 1
    #print("keeper:", keeper.upper())
    return keeper.upper()

create_an_acronym()

