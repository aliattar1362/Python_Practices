"""
COMP.CS.100: A Tourist Dictionary
Creator: Mohsen Haajari
Student id number: 150987659
Learning Goals
I review the basic operations of a dictionary (dict).
"""

def main():
    """
    COMP.CS.100: Price List
    Creator: Mohsen Haajari
    Student id number: 150987659
    """
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}
    english_spanish = dict(sorted(english_spanish.items()))
    while True:
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":
            word = input("Enter the word to be translated: ")
            if word in english_spanish:
                print(word, "in Spanish is", english_spanish[word])

            else: 
                print("The word", word, "could not be found from the dictionary.")
            #print()
            
        elif command == "A":
            add_en = input("Give the word to be added in English: ")
            add_sp = input("Give the word to be added in Spanish: ")
            english_spanish.update({add_en: add_sp})
            print()    
            
        elif command == "R":
            rem_word = input("Give the word to be removed: ")
            
            if rem_word in english_spanish:
                del english_spanish[rem_word]
            else:
                print("The word", rem_word, "could not be found from the dictionary.")
            print()
            
        elif command == "Q":
            print("Adios!")
            False
            return
            print()

        elif command == "P":
            english_spanish = dict(sorted(english_spanish.items()))
            for word in english_spanish:
                print(word, english_spanish[word])
            print()
                
        elif command == "T":

            text = []
            input_text = input("Enter the text to be translated into Spanish: ")  
            print("The text, translated by the dictionary:")
            text = input_text.split()
            #new_text = ""
            for word in text:
                if word in english_spanish:
                    #new_text += word
                    print(english_spanish[word], end=" ")
                else:
                    print(word, end=" ")
            print()

if __name__ == "__main__":
    main()
