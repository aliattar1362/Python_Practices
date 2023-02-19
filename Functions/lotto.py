"""
Implement a program that asks the user for two input values:
the amount of lottery balls (or numbers) and
the drawn balls (or numbers).
and then prints the probability of getting a jackpot with only 
one coupon (1 divided with the number of different lottery lines)
. Additionally have the program print the following error messages:
"The number of balls must be a positive number."
"At most the total number of balls can be drawn."
The total number of balls and the number of drawn balls are always 
asked before checking for errors. First thing to check is whether 
the numbers of balls are positive. If there is an error, 
print an error message and terminate the program's run immediately. 
If both entered numbers are positive, check the numbers of the balls. 
An error message is also printed in this case there is an error, 
and the program's run is terminated.
"""
def factorial_func(number):
    """
    This is the functino to calculate factorial value for each input number.
    :number: Entered number (int).
    :fac: Output number that is calculated Factorial based on entered number.
    """
    if number == 0:
        fac = 1
    else:
        # Initialize factorial for 0 (0! = 1).
        fac = 1
        for number in range(1, number+1):
            fac *= number
    # Return the vaue for factorial.
    return fac

def combination_func(n, p):
    """
    This is the functino to calculate the combination based on two enterd number
    here are n and p, respectively.
    :n: first value (int)
    :p: second value (int)
    """
    n_fac = factorial_func(n)
    n_minus_p_fac = factorial_func(n - p)
    p_fac = factorial_func(p)
    formula = (n_fac/(n_minus_p_fac * p_fac))
    return formula
    

def main():
    """
    This is the main functino to print the chance of winning lottery after
    buying 1 ticket according to the number of total lottery balls and number
    of drawn balls.
    Here we ask these values by input function.
    :lottery_balls: first value (int)
    :drawn_balls: second value (int)
    """
    lottery_balls = int(input("Enter the total number of lottery" + \
                                " balls: "))
    drawn_balls = int(input("Enter the number of the drawn balls: "))
    if not lottery_balls > 0:
        print("The number of balls must be a positive number.")
    else:
        if drawn_balls > lottery_balls:
            print("At most the total number of balls can be drawn.")
        else:
            result = combination_func(lottery_balls, drawn_balls)
            print("The probability of guessing all ", drawn_balls, " balls" + \
                  " correctly is 1/", format(result, ".0f"), sep="")
        
main()