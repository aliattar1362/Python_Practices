"""
Learning Goals
Learning about using arithmetic operators in Python
and making calculations with integers.
"""
# Create a program that asks how much purchases cost 
# and the amount of paid money and then prints the 
# amount of change. Simplify the program by only allowing 
# the use of sums of 1, 2, 5 and 10 euros. Ensure that 
# the total price is always in full euros.

def main():
    
    # Get purchase price
    purchase_price = int(input("Purchase price: "))
    
    # Get the paid amount of money
    paid_money = int(input("Paid amount of money: "))
    
    # Calculate the money should be returned.
    return_money = paid_money - purchase_price
    
    #Calculate 
    tenth = return_money // 10
    remain_tenth = return_money % 10
    fifth = remain_tenth // 5
    remain_fifth = remain_tenth % 5
    twice = remain_fifth // 2
    oneth = remain_fifth % 2
     
    
    if return_money <= 0:
        print("No change")
        
    else:
        print("Offer change:")
        if tenth > 0 :
            if fifth > 0:
                if twice > 0:
                    if oneth > 0:
                        print(tenth, "ten-euro notes")
                        print(fifth, "five-euro notes")
                        print(twice, "two-euro coins")
                        print(oneth, "one-euro coins")
                    else:
                        print(tenth, "ten-euro notes")
                        print(fifth, "five-euro notes")
                        print(twice, "two-euro coins")
                else:
                    if oneth > 0:
                        print(tenth, "ten-euro notes")
                        print(fifth, "five-euro notes")
                        print(oneth, "one-euro coins")
                    else:
                        print(tenth, "ten-euro notes")
                        print(fifth, "five-euro notes")
            else:
                if twice > 0:
                    if oneth > 0:
                        print(tenth, "ten-euro notes")
                        print(twice, "two-euro coins")
                        print(oneth, "one-euro coins")
                    else:
                        print(tenth, "ten-euro notes")
                        print(twice, "two-euro coins")
                else:
                    if oneth > 0:
                        print(tenth, "ten-euro notes")
                        print(oneth, "one-euro coins")
                    else:
                        print(tenth, "ten-euro notes")
        else:
            if fifth > 0:
                if twice > 0:
                    if oneth > 0:
                        print(fifth, "five-euro notes")
                        print(twice, "two-euro coins")
                        print(oneth, "one-euro coins")
                    else:
                        print(fifth, "five-euro notes")
                        print(twice, "two-euro coins")
                else:
                    if oneth > 0:
                        print(fifth, "five-euro notes")
                        print(oneth, "one-euro coins")
                    else:
                        print(fifth, "five-euro notes")
            else:
                if twice > 0:
                    if oneth > 0:
                        print(twice, "two-euro coins")
                        print(oneth, "one-euro coins")
                    else:
                        print(twice, "two-euro coins")
                else:
                    print(oneth, "one-euro coins")
                    
if __name__ == "__main__":
    main()
