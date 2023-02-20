"""
Learning Goals
Considering sorting the dict in even more detail.
"""

def main():
    
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}
    english_spanish = dict(sorted(english_spanish.items()))
    print("Dictionary contents:")
    counter = 0
    word_list = list(english_spanish.keys())    
    while not counter == len(word_list)-1:
        print(f"{word_list[counter]}, ", end="")
        counter += 1
    print(f"{word_list[counter]}")
    
    while True:
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":

            word = input("Enter the word to be translated: ")
            if word in english_spanish:
                print(word, "in Spanish is", english_spanish[word])

            else: 
                print("The word", word, "could not be found from the dictionary.")
                print()

        elif command == "A":
            add_en = input("Give the word to be added in English: ")
            add_sp = input("Give the word to be added in Spanish: ")
            english_spanish.update({add_en: add_sp})
            english_spanish = dict(sorted(english_spanish.items()))
            print("Dictionary contents:")
            counter = 0
            word_list = list(english_spanish.keys())    
            while not counter == len(word_list)-1:
                print(f"{word_list[counter]}, ", end="")
                counter += 1
            print(f"{word_list[counter]}")
            #print()
            
            
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
            print()
            print("English-Spanish")
            english_spanish = dict(sorted(english_spanish.items()))
            for word in english_spanish:
                print(word, english_spanish[word])
                
            print()  
            spanish_english = dict(sorted(english_spanish.items(), key=lambda item: item[1]))
            spanish_english_keys = list(spanish_english.values())
            spanish_english_list = list(spanish_english.keys())
            index = 0
            print("Spanish-English")
            for word in spanish_english_keys:
                print(word, spanish_english_list[index])
                index += 1
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
    
        else:
            print("Unknown command, enter W, A, R, P, T or Q!")
            print()

if __name__ == "__main__":
    main()
