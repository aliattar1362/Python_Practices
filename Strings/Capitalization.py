"""
Learning goals:
Getting acquainted with string methods in Python. 
Learning to use Python's documentation.
"""    
def capitalize_initial_letters(text = "Aatu beetu CEETU Deetu eETU Feetu geetu Heetu IITU jiitu"):

    text = text.lower()
    text = text.split()
    #print("text:", text)
    count = 0
    keeper = ""
    #print("len(text):", len(text))
    while not count == len(text):
            word = text[count]
            first_letter = word[0]
            remain_letters = word[1:]
            keeper += first_letter.upper()  \
                        + remain_letters + " "  
            count += 1
    #print("keeper:", keeper)
    return keeper


