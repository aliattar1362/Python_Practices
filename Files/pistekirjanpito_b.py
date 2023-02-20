"""
Learning Goals:
I learn to handle the error situations when 
processing information that is stored in a file.
"""

############################################################        
        
def main():
        
    filename = input("Enter the name of the score file: ")

    try:
        file = open(filename, mode="r")

    except OSError:
         #print(f"Error: opening the file '{filename}' failed!")
         print("There was an error in reading the file.")
         return
    
    my_dict = {}
    my_list = []
    for file_line in file:
        my_list = file_line.split(" ")
        #print(file_line[1])
        #print(my_list)
        name = my_list[0]
        #print(name)
        score = my_list[1]
        #score = score.replace('\n', '')
        try:
            score = int(score)
            #print(score)
            if not name in my_dict:
                my_dict.update({name: score})
                #print("no")
                #print(name)
            else:
                my_dict[name] += score
        
        except ValueError:
             print("There was an erroneous score in the file:")
             print(score)
             return
        
        except IndexError:
            print("There was an erroneous score in the file:")
            print(IndexError) 
            return
        
    my_dict = dict(sorted(my_dict.items())) 
    #print(my_dict)
    print("Contestant score:")
    for keys, value in my_dict.items() :
        print(f"{keys} {value}")
    
       
    file.close()

if __name__ == "__main__":
    main()
