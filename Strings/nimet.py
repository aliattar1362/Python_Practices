   
def reverse_name(text = "Techie, Teddy"):
    """
    This is the main function. It calls several fucntions. 
    First calls get_input fucntinos to make the list.
    Then calls the functinos to calculate the desired 
    statistical values.
    """
    #text = "Techie, Teddy"
    count = text.count(",")
    #print("count:", count)
    if count == 0:
        text = text.strip()
        return text
    else:
        word_list = text.split(",")
        #print("word_list:", word_list)
        first_name = word_list[1].strip() 
        #print("first_name:", first_name)
        #print("len(first_name):", len(first_name))
        family_name = word_list[0].strip()
        #print("family_name:", family_name)
        #print("len(family_name):", len(family_name))
        
        if len(first_name) == 0:
            return family_name
        elif len(family_name) == 0:
            return first_name
        else:
            full_name = first_name + " " + family_name
            return full_name

