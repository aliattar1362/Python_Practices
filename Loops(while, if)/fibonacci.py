def main():
    # Initialize Fibonacci number for 1 and 2
    f_1 = 1
    f_2 = 1
    # Get how many Fibonacci numbers does user want?
    number = int(input('How many Fibonacci numbers do you want? '))
    if number == 1:
        print ('1.', f_1)
    elif number == 2:
        print ('1.', f_1)
        print ('2.', f_2)
    else:
        print ('1.', f_1)
        print ('2.', f_2)
        previous_fib = 1
        current_fib = 1
        for i in range(3, number+1):
            next_fib = current_fib + previous_fib
            print(i,'. ', next_fib, sep='')
            previous_fib = current_fib
            current_fib = next_fib

if __name__ == "__main__":
    main()
