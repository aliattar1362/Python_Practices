 
def get_input():
    """
    This is the main function. It calls several fucntions. 
    First calls get_input fucntinos to make the list.
    Then calls the functinos to calculate the desired 
    statistical values.
    """
    word = input("Enter a word: ")
    return word

def word_seperator(word):
    """
    This is the main function. It calls several fucntions. 
    First calls get_input fucntinos to make the list.
    Then calls the functinos to calculate the desired 
    statistical values.
    """
    v_counter = 0
    for l in word:
        if l=="a"  or l=="e" or l=="i" or l=="o" or l== "u" or l== "y":
            v_counter += 1
    # Consonant counter: Numbers of consonants
    c_counter = len(word) - v_counter
    
    return v_counter, c_counter
    
def main():
    """
    This is the main function. It calls several fucntions. 
    First calls get_input fucntinos to make the list.
    Then calls the functinos to calculate the desired 
    statistical values.
    """
    word = get_input()
    v_counter, c_counter = word_seperator(word)
    print(f"The word \"{word}\" contains {v_counter} "
          f"vowels and {c_counter} consonants.")
    
if __name__ == "__main__":
    main()

