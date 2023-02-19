def print_verse(animal, voice):
    """
    This function operates the verse by inserting the name of
    animals and their voices.
    """
    print('Old MACDONALD had a farm')
    print('E-I-E-I-O')
    print('And on his farm he had a', animal)
    print('E-I-E-I-O')
    print('With a', voice, voice, 'here')
    print('And a', voice, voice, 'there')
    print('Here a ', voice, ', there a ', voice, sep='')
    print('Everywhere a', voice, voice)
    print('Old MacDonald had a farm')
    print('E-I-E-I-O')
    print()
    
def main():
    """
    This is the main functino to operate the "print_verse(animal, voice)"
    to display the lyrics
    """
    print_verse("cow", "moo")
    print_verse("pig", "oink")
    print_verse("duck", "quack")
    print_verse("horse", "neigh")
    print_verse("lamb", "baa")
        
if __name__ == "__main__":
    main()
