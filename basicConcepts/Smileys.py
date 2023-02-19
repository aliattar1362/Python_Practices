"""
Learning Goals
Review if, elif, and else.
"""
# Create a program that asks the user how they feel on
# scale 1-10 and then proposes a suitable emoticon to 
# describe the mood. First implement a relatively expression
# less version that prints :-) for feelings over 7 and
# otherwise prints the basic face :-|.
# Now make the previously mentioned program verify the
# numeric values - if something other than a numeric 
# value between 1 and 10 is entered, the program should 
# print Bad input!
# You should be able to express negative emotions when
#  necessary, so let’s add the program a sad 
# emoticon :-(, which is recommended for feelings that are
# less than 4.
# d) Let’s add more expressiveness to the program.
# The extremes of the emotion scale, the values 1 and 10, 
# use the stronger faces :'( and :-D.

def main():
    
    # Get the feeling score in int form
    feeling_score = int(input("How do you feel? (1-10) "))
    # The condition for emoticon correlated to feeling score
    # and print the proper text
    if feeling_score == 1:
        print("A suitable smiley would be :'(")
        
    
    
    elif feeling_score > 1 and  feeling_score < 4:
        print("A suitable smiley would be :-(")
    
    elif feeling_score > 3 and feeling_score <= 7:
        print("A suitable smiley would be :-|")
        
    elif feeling_score > 7 and feeling_score < 10:
        print("A suitable smiley would be :-)")
        
    elif feeling_score == 10:
        print("A suitable smiley would be :-D")
        
    else:
        print("Bad input!")
    
if __name__ == "__main__":
    main()
