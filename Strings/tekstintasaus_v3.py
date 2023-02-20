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

    #print(type(text))
    #print(text)
    #print("len(text):", len(text))
    if len(text) > char:
        text = text.split()
        #print(type(text))
        #print(text)
        index = 0
        total_text = ""
        #len(total_text)
        #print("len(total_text)", len(total_text))
        while not (len(total_text)+(index+1)+len(text[index]))>char:
            total_text += text[index]
            index += 1
            #print("total_text:", total_text)
            #print("len(total_text)", len(total_text))
            #print("index:", index)
        differ = char - len(total_text)
        #print("differ: ", differ)
        my_text = ""
        counter = 0
        while not counter == index:
            if counter < index-1:
                my_text += text[counter] + (differ//(index-1) * " ")
                #print(f"text_{counter}:", text[counter])
                #print("my_text:", my_text)
                #print(len(my_text))
                if counter < (differ % (index-1)):
                    my_text += " "
            else:
                my_text += text[counter]
                
            #print(len(my_text))
            counter += 1
            
        #print("my_text:", my_text)
        #print("len(my_text): ", len(my_text))
        text = text[index:]
        #print("len(text):",len(text))
        #print(text)
        #print(my_text)
        #print(len(my_text))
        #print(len(text))
        return my_text, text
    else:
        #print(text)
        my_text = text
        text = ""
        #print(text)
        #print(my_text)
        #print(len(my_text))
        #print(len(text))
        return my_text, text
#justify_text()





def list_to_str(text):

    new_text = ""
    for word in text:
        new_text += word + " "
    return new_text
        

def main():
    
    text = read_message()
    #print(len(text))
    #print(text)
    char = number_of_charachter()
    text_line, remain_text = justify_text(text, char)
    text = list_to_str(remain_text)
    #print(len(text))
    #print(text)
    #print(type(text))
    #print(len(text_line))
    print(text_line)
    #print(len(remain_text))
    #print(remain_text)
    while not len(text) < char:
        #print("hello")
        #print("len(text_line):", len(text_line))
        text_line, remain_text = justify_text(text,char)
        #print("Yexy")
        text = list_to_str(remain_text)
        print(text_line)
        #print("remain_text:", remain_text)
    if len(remain_text) < char:
        text = list_to_str(remain_text)
        text_line, remain_text = justify_text(text, char)
          
if __name__ == "__main__":
    main()

