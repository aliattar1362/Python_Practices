"""
Learning goals:
Learning to design a somewhat more challenging algorithm 
for processing strings.
""" 
def count_abbas(text = "abcabcdefgabab"):
    """
    This is the abba counter fucntion
    """ 
    counter = 0
    
    while "abba" in text:
        print(text)
        counter += 1
        print((text.find('abba')))
        text = text[(text.find('abba') + 3):]
        print(text)
    print(counter)
        
    
count_abbas(text = "abbabbabba")