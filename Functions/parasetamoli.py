def calculate_dose(weight, time, dose):
    """
    An adult patient in doses of 15 mg per kilogram of weight,
    once every six hours
    """
    first_consume = weight * 15
    if time >= 6:
        if dose < 4000:
            final_amount = 4000 - dose
            while final_amount > first_consume:
                    final_amount = first_consume
                    break
        else:
            final_amount = 0
    else:
        final_amount = 0

    return final_amount

def main():
    weight = int(input("Patient's weight (kg): "))
    time = int(input("How much time has passed from " + \
                     "the previous dose (full hours): "))
    
    dose = int(input("The total dose for the " + \
                            "last 24 hours (mg): "))
    amount = calculate_dose(weight , time, dose)
    print("The amount of Parasetamol to " + \
          "give to the patient:", amount)

    # calculate_dose assumes parameters to be of type int
    # and they should be passed in the order: weight, time, total_doze_24
    # (or more like the automated tests assume this)
if __name__ == "__main__":
  main()
