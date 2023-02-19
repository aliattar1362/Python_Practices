"""
Learning goals:
I learn to use a datastructure that contains 
multiple strings.

Challenging Assignment
This os one of the challenging assignments for 
those who are seeking purpose for their life. 
Point gain is miserly but your ego will burst 
out of its seams if you succeed.
"""  

def read_message():
    """This function get the text from justify_text() fucntion
    and convert the text format from list to string. Finally it
    transfers the text to the justify_text() fucntion for 
    further processing.
    :text: list type as input
    :text: str type for output.
    """
    print("Enter text rows. Quit by ", end="") 
    print("entering an empty row.")
    text = input("")
    new_text = ""
    while not text == "":
        new_text += text
        text = input("")
    return new_text

def number_of_charachter():
    """This function get the text from justify_text() fucntion
    and convert the text format from list to string. Finally it
    transfers the text to the justify_text() fucntion for 
    further processing.
    :text: list type as input
    :text: str type for output.
    """
    char = input("Enter the number of characters per line: ")
    char = int(char)
    return char
    

def justify_text(text, char):
    """This function get the text from justify_text() fucntion
    and convert the text format from list to string. Finally it
    transfers the text to the justify_text() fucntion for 
    further processing.
    :text: list type as input
    :text: str type for output.
    """
    text = text.split()
    new_text = ""
    index = 0
    while not index == len(text):
        len_word = len(text[index])
        #print("len_word", len_word)
        len_text = len(new_text)
        #print("len_text", len_text)
        len_total = len_word + len_text 
        #print("len_total", len_total)
        #print("text[index]: ", text[index])
        if len_total < char:
            #print("index:", index)
            new_text += text[index] + " "
            #print("new_text:", new_text)
            #print("len(new_text): ", len(new_text))
            #print(text[index])
            #print(len(text[index]))
            my_line = new_text    
        elif len_total == char:
            #print("index:", index)
            new_text += text[index]
            #print("new_text:", new_text)
            #print("len(new_text): ", len(new_text))
            #print(text[index])
            #print(len(text[index]))
            my_line = new_text
        elif len_total > char:
            differ = char - len(new_text)
            new_text = new_text.split()
            #print("new_text:", new_text)
            #print("len(new_text): ", len(new_text))
            #print("differ: ", differ)
            counter = 0
            my_line = ""
        
            for word in new_text:
                #print("counter: ", counter)
                if counter < differ:
                    #print("if")
                    my_line += word + " "
                    my_line += (differ//index * " " + " ")
                else:
                    #print("else")
                    my_line += word + " "
                    my_line += (differ//index * " ")
                counter += 1
            
            #print(my_line)
            #print(len(my_line))
            #print(index)
            text = text[index:]
            #print("text:", text)
            #
            break
        index += 1 
    #print(type(text)) 
    #print(my_line)
    #print(len(my_line))
    return my_line, text

def text_box(text):
    """This function get the text from justify_text() fucntion
    and convert the text format from list to string. Finally it
    transfers the text to the justify_text() fucntion for 
    further processing.
    :text: list type as input
    :text: str type for output.
    """
    new_text = ""
    for word in text:
        new_text += word + " "
    #print(new_text)  
    #print(type(new_text))
    return new_text


def main():
    
    """CHAPTER VIII - CONCERNING THOSE WHO HAVE 
    OBTAINED A PRINCIPALITY BY WICKEDNESS
Although a prince may rise from a private station in two ways,
 neither of which can be entirely attributed to fortune 
 or genius, yet it is manifest to me that I must not be 
 silent on them, although one could be more copiously treated 
 when I discuss republics. These methods are when, either by 
 some wicked or nefarious ways, one ascends to the 
 principality, or when by the favour of his fellow-citizens 
 a private person becomes the prince of his country. 
 And speaking of the first method, it will be illustrated 
 by two examples--one ancient, the other modern--and without 
 entering further into the subject, I consider these 
 two examples will suffice those who may be compelled to 
 follow them."""
 
    text = read_message()
    last_text = ""
    char = number_of_charachter()
    each_line, remain_text = justify_text(text, char)
    print(each_line)
    for i in range(char*1000):
        last_text = each_line
        #print(last_text)
        text = text_box(remain_text)
        each_line, remain_text = justify_text(text, char)
        if not each_line == last_text:
            print(each_line)
            #print(len(text))
            text = text_box(remain_text)
            #print(len(text))
        else:
            break
        
         
if __name__ == "__main__":
    main()
    


