"""
Learning goals:
Learning to design a somewhat more challenging algorithm for 
processing strings.
""" 
def longest_substring_in_order (text = "efghijklmnopopqefgabcdeabcdefghijklm"):
    """
    This is the abba counter fucntion
    """ 
    if len(text) == 0:
        return text
    else:
        index = 0
        new_text = text[0]
        answer = text[0]
        while not index == len(text)-1:
        
            if text[index] < text[index+1]:
            #print(text[index] < text[index+1])
                new_text += text[index+1]
                #print("new_text:", new_text)
                #print("len(new_text):", len(new_text))
                #print("answer:", answer)
                #print("len(answer):", len(answer))
                if len(answer) < len(new_text):
                    answer = new_text
                elif len(answer) == len(new_text):
                    if answer <= new_text:
                #print("answer <= new_text", answer <= new_text)
                        answer = new_text
                #print("answer:", answer)
            #print("answer:", answer)
            else:
            #print(text[index] < text[index+1])
                new_text = text[index+1]
            #print("text[index+1]:", text[index+1])
            #print("new_text:", new_text)
        #print("[index]", [index])
        #print("text[index]:" ,text[index])
        #print("text[index+1]:", text[index+1])
            index += 1
        #print(answer)
        return answer

#longest_substring_in_order()