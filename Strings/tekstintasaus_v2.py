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

    print("Enter text rows. Quit by ", end="") 
    print("entering an empty row.")
    text = input("")
    new_text = ""
    while not text == "":
        new_text += text
        text = input("")
    return new_text

def number_of_charachter():

    char = input("Enter the number of characters per line: ")
    char = int(char)
    return char
    

def justify_text(text, char):

    text = text.split()
    index = 1
    total_text = text[0] + " " 
    while not index == len(text):
        #print("total_text:", total_text)
        #print("len_total_text:", len(total_text))
        #print(f"word {index}: ", text[index])
        len_word = len(text[index]) 
        #print("len_word:", len_word)
        len_total_text = len(total_text) 
        #print("len_total_text:", len_total_text)
        len_total = len_word + len_total_text 
        #print("len_total", len_total)
        if len_total < char:
            #print("index:", index)
            total_text += text[index] 
            if len(total_text) < char:
                total_text += " "
            #print("total_text:", total_text)
            #print("len(total_text): ", len(total_text))
            #print(text[index])
            #print(len(text[index]))
            my_line = total_text    
        elif len_total == char:
            #print("index:", index)
            total_text += text[index]
            #print("total_text:", total_text)
            #print("len(total_text): ", len(total_text))
            #print(text[index])
            #print(len(text[index]))
            my_line = total_text
        elif len_total > char:
            differ = char - len(total_text)
            total_text = total_text.split()
            #print("total_text:", total_text)
            #print("len(total_text): ", len(total_text))
            #print("differ: ", differ)
            counter = 0
            my_line = ""
        
            for word in total_text:
                #print("counter: ", counter)
                if counter < differ:
                    #print("if")
                    my_line += word + " "
                    my_line += (differ//index * " ")
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
    #print("len(my_line):", len(my_line))
    return my_line, text

def text_box(text):

    new_text = ""
    for word in text:
        new_text += word + " "
    #print(new_text)  
    #print(type(new_text))
    return new_text


def main():
 
    text = read_message()
    last_text = ""
    char = number_of_charachter()
    each_line, remain_text = justify_text(text, char)
    print(each_line)
    for i in range(char*100000):
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
    


