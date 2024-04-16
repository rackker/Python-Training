## error & exception handling ##

# LBYL look before you leap coding style - use if statements to check if action is possible
# LBYL avoids raising exceptions 

def calculate_ratio_lbyl(boys,girls):
    if girls != 0:
        print(boys / girls)
    else:
        print("There are no girls")

calculate_ratio_lbyl(58,33)
calculate_ratio_lbyl(34,0)

# EAFP easier to ask for forgiveness rather than permissions - this is the Pythonic approach

def calculate_ratio_eafp(boys,girls):
    try:
        print(boys / girls)
    except ZeroDivisionError:
        print("you cant devide by zero")

calculate_ratio_eafp(58,33)
calculate_ratio_eafp(34,0)