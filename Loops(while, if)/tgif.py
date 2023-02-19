
def main():
    # Initialize first month.
    m = 1
    # Initialize first Friday of 2014.
    f = 3
    while m == 1:
        print(f, '.', m, '.', sep='') 
        f += 7
        if f > 31:
            f -= 31
            m += 1
    while m == 2:
        print(f, '.', m, '.', sep='') 
        f += 7
        if f > 28:
            f -= 28
            m += 1
    while m == 3:
        print(f, '.', m, '.', sep='') 
        f += 7
        if f > 31:
            f -= 31
            m += 1
    while m == 4:
        print(f, '.', m, '.', sep='') 
        f += 7
        if f > 30:
            f -= 30
            m += 1
    while m == 5:
        print(f, '.', m, '.', sep='') 
        f += 7
        if f > 31:
            f -= 31
            m += 1
    while m == 6:
        print(f, '.', m, '.', sep='') 
        f += 7
        if f > 30:
            f -= 30
            m += 1
    while m == 7:
        print(f, '.', m, '.', sep='') 
        f += 7
        if f > 31:
            f -= 31
            m += 1
    while m == 8:
        print(f, '.', m, '.', sep='') 
        f += 7
        if f > 31:
            f -= 31
            m += 1
    while m == 9:
        print(f, '.', m, '.', sep='') 
        f += 7
        if f > 30:
            f -= 30
            m += 1
    while m == 10:
        print(f, '.', m, '.', sep='') 
        f += 7
        if f > 31:
            f -= 31
            m += 1
    while m == 11:
        print(f, '.', m, '.', sep='') 
        f += 7
        if f > 30:
            f -= 30
            m += 1
    while m == 12:
        print(f, '.', m, '.', sep='') 
        f += 7
        if f > 31:
            f -= 31
            m += 1
            
if __name__ == "__main__":
    main()
