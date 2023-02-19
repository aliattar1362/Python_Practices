
def main():
    for m in range(1, 12+1):
        if m == 1 or m == 3 or m == 5 or m == 7 or \
            m == 8 or m == 10 or m == 12:
                for d in range (1, 31+1):
                   print(d, '.', m, '.', sep='') 
                
        elif m == 2:
            for d in range (1, 28+1):
                print(d, '.', m, '.', sep='') 
                
        else:
            for d in range (1, 30+1):
                print(d, '.', m, '.', sep='') 
                
if __name__ == "__main__":
    main()
