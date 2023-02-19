"""
Learning Goals

Learning to use variables and calculate statement values.
"""
# This program asks how much study benefits the user receives
# and calculates how a 1,17 percent index raise affects the
# benefits.

# Define index raise as a global variable that is 1.17%.
INDEX_RAISE = 1.0117

# Get the amount of the study benefits: 335.32.
study_benefit = float(input("Enter the amount of the " \
                            "study benefits: "))

# Display the final text and calculate the new study benefit.
study_benefit = study_benefit * INDEX_RAISE
print("If the index raise is 1.17 percent, the study benefit,")
print("after a raise, would be", study_benefit, 'euros')

# Display the next effect of index raise on study benefit.
study_benefit = study_benefit * INDEX_RAISE
print("and if there was another index raise, the study")
print("benefits would be as much as", study_benefit, 'euros')