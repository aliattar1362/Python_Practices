"""
Learning Goals:
Lists are often processed using a for loop and a range 
function, so the purpose of the first task is reviewing 
how the for and range operate.
"""

def main():
    """
prints the even numbers from 0 to 100 in an ascending order, 
and then the same numbers in descending order. Each number is 
printed on its own row.
    """
    for i in range(0, 101, 2):
        print (i)
    for j in range(100, -1, -2):
        print (j)
        
if __name__ == "__main__":
    main()
