"""
Learning Goals:
To understand, that if a function modifies the elements 
of a list it received as a parameter, the modifications 
also affect the actual parameter at the point where the 
function was called.
"""     
 
# TODO: add the definition for convert_grades here
def convert_grades(grades):

    fail_grade = 0
    pass_grade = 6
    if len(grades) > 0:
        index = 0
        while not len(grades) == index:
            if grades[index] > 0:
                grades[index] = pass_grade
            else:
                grades[index] = fail_grade
            index +=1
            
def main():

    grades = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0]
    convert_grades(grades)
    print(grades)  # Should print [0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0]

if __name__ == "__main__":
    main()

