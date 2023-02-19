"""
Learning Goals:
Learning to implement functions that contain calculations.
Important

This assignment is quite challenging. The reason for why this 
complex problem only gives 1 basic point is so that no one 
feels they have to finish it. If you skip the assignment, 
one point lost doesn't make or break anyones day. 
But there are some students who like having adventure 
and excitement in their life, this problem is for them.
"""
from math import sqrt

# Global vaiable for constant distance unit
DISTANCE_UNIT = 100 # Kilometers

def menu():
    """
    This is a text-based menu. You should ONLY TOUCH TODOs inside the menu.
    TODOs in the menu call functions that you have implemented and take care
    of the return values of the function calls.
    """
    tank_size = read_number("How much does the vehicle's gas tank hold? ")
    gas = tank_size  # Tank is full when we start
    gas_consumption = read_number("How many liters of gas does the car " +
                                  "consume per hundred kilometers? ")
    x = 0.0  # Current X coordinate of the car
    y = 0.0  # Current Y coordinate of the car

    while True:
        print("Coordinates x={:.1f}, y={:.1f}, "
              "the tank contains {:.1f} liters of gas.".format(x, y, gas))
        # \n: Go to next line for continue of text
        choice = input("1) Fill 2) Drive 3) Quit\n-> ")

        if choice == "1":
            to_fill = read_number("How many liters of gas to fill up? ")
            gas = fill(tank_size, to_fill, gas)

        elif choice == "2":
            new_x = read_number("x: ")
            new_y = read_number("y: ")
            gas, x, y = drive(x, y, new_x, new_y, gas, gas_consumption)

        elif choice == "3":
            break

    print("Thank you and bye!")


def fill(tank_size, to_fill, gas):
    """
    This function has three parameters which are all FLOATs:
      (1) the size of the tank
      (2) the amount of gas that is requested to be filled in
      (3) the amount of gas in the tank currently

    The parameters have to be in this order.
    The function returns one FLOAT that is the amount of gas in the
    tank AFTER the filling up.

    The function does not print anything and does not ask for any
    input.
    """
    # Calculate the empty volume in tank as empty_capacity parameter
    empty_capacity = tank_size - gas
    # Check the added fule is higher than empty_capacity or not:
    if to_fill >= empty_capacity:
        # If added gas is higher, then it cannot be higher than
        # empty_capacity. it means that the Tank will be filled up to 
        # tank size
        gas = tank_size
    else:
        # If added gas is not higher than the empty space, then 
        # the gas amount is current gas plus added gas
        gas += to_fill
    return gas 



def drive(x, y, new_x, new_y, gas, gas_consumption):
    """
    This function has six parameters. They are all floats.
      (1) The current x coordinate
      (2) The current y coordinate
      (3) The destination x coordinate
      (4) The destination y coordinate
      (5) The amount of gas in the tank currently
      (6) The consumption of gas per 100 km of the car

    The parameters have to be in this order.
    The function returns three floats:
      (1) The amount of gas in the tank AFTER the driving
      (2) The reached (new) x coordinate
      (3) The reached (new) y coordinate

    The return values have to be in this order.
    The function does not print anything and does not ask for any
    input.
    """
    # Here the aimed distance is calculated based on enterd data
    distance = distance_func(x, y, new_x, new_y)
    # Here needed gas is calculated based on aimed distance, gas amount 
    # and gas consumption rate.
    needed_gas = needed_gas_func(distance, gas, gas_consumption)
    # Define condition according to amount of needed gas
    if needed_gas > gas:
        # It means that a portion of distance cannot be passed by car because
        # Lack of gas. Accordingly, this amount is calculated here
        lost_distance = (needed_gas - gas) * DISTANCE_UNIT / gas_consumption
        # Here the passed distance that is the actual distance is calculated
        # as new distance. The formula in course material is useful.
        new_distance = distance - lost_distance # == P in course material
        # Calculate the delta x and delta y based on the formula.
        delta_x = new_distance * (new_x - x)/ distance
        delta_y = new_distance * (new_y - y)/ distance
        # Here the x, y and gas are updated
        gas = 0
        x += delta_x
        y += delta_y
    else:
        gas -= needed_gas
        x = new_x
        y = new_y
        
    return gas, x, y


def needed_gas_func(distance, gas, gas_consumption):
    """
    This function has four parameters. They are all floats.
      (1) The passed distance between two points
      (2) the gas amount in tank
      (3) the gas consumption per 100 KM

    The function returns one floats:
      (1) needed_gas by car to travel from initial point to target point.
    """
    # Following formulais used to calculate needed gas to travell 
    # this distance
    needed_gas = (distance * gas_consumption) / DISTANCE_UNIT
    return needed_gas
    

    # It might be usefull to make one or two assisting functions
    # to help the implementation of this function.
    
def distance_func(x, y, new_x, new_y):
    """
    This function has four parameters. They are all floats.
      (1) The current x coordinate
      (2) The current y coordinate
      (3) The destination x coordinate
      (4) The destination y coordinate

    The function returns one floats:
      (1) The distance passed by car
      This function uses Pythagorean theorem to calculate passed distance.
    """
    distance = sqrt((new_x - x) ** 2 + (new_y - y) ** 2)
    return distance



def read_number(prompt, error_message="Incorrect input!"):
    """
    DO NOT TOUCH THIS FUNCTION.
    This function reads input from the user.
    Also, don't worry if you don't understand it.
    """

    try:
        return float(input(prompt))

    except ValueError:
        print(error_message)
        return read_number(prompt, error_message)

def main():
    menu()
    

if __name__ == "__main__":
    main()


