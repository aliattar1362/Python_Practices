
def verse(text_1, text_2):
    """
    This function operates the verse by inserting the name of
    animals and their voices.
    """
    print(text_1)
    print(text_2, ', ', text_2, sep='')
    print(text_1)
    for i in range(3):
        print(text_2, ', ', text_2, ' Bear', sep='')
    print(text_1)
    print(text_2, ', ', text_2, ' Bear', sep='')
    print()
    

def main():
    verse("I know someone you don't know", "Yogi")
    verse("Yogi has a best friend too", "Boo Boo")
    verse("Yogi has a sweet girlfriend", "Cindy")


if __name__ == "__main__":
    main()
