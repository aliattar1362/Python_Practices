def print_verse(animal,voice):
    """
    This function operates the verse by inserting the name of
    animals and their voices.
    """

    string="""Old MACDONALD had a farm
E-I-E-I-O
And on his farm he had a {0}
E-I-E-I-O
With a {1} {1} here
And a {1} {1} there
Here a {1}, there a {1}
Everywhere a {1} {1}
Old MacDonald had a farm
E-I-E-I-O\n"""
    print(string.format(animal,voice))

def main():
    """
    This is the main functino to operate the 
    "print_verse(animal, voice)" to display the lyrics
    """
    print_verse("cow", "moo")
    print_verse("pig", "oink")
    print_verse("duck", "quack")
    print_verse("horse", "neigh")
    print_verse("lamb", "baa")
main()