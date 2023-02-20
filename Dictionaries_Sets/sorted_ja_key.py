"""
Learning Goals
I will learn to use the key parameter for 
the sorted function.
"""
PRICES = {"milk": 1.09, "fish": 4.56, "bread": 2.10,
        "chocolate": 2.70, "grasshopper": 13.25,
        "sushi": 19.90, "noodles": 0.97, "beans": 0.87,
        "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,}

def main():
    my_dic = dict(sorted(PRICES.items(), key=lambda item: item[1]))
    pass
    for keys, value in my_dic.items() :
        print(f"{keys} {value:.2f}")

if __name__ == "__main__":
    main()
