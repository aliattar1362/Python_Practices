"""
Learning Goal
I will understand how to index dict data structure 
to find the payload connected to the key.
"""

PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.7, "grasshopper": 13.25,
    "sushi": 19.9, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}


def main():
    product_name = input("Enter product name: ")
    product_name = product_name.strip()
    #print(product_name)
    #print(len(product_name))
    while not len(product_name) == 0:
        if product_name in PRICES:
            print(f"The price of {product_name} is ", end="")
            print(f"{PRICES[product_name]:.2f} e")
        else:
            print(f"Error: {product_name} is unknown.")
        product_name = input("Enter product name: ")
        product_name = product_name.strip()
    
    if len(product_name) == 0:
        print("Bye!")
if __name__ == "__main__":
    main()

