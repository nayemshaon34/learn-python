weight = input("Weight: ")
unit = input("(L)bs or (K)g: ")

if unit.lower() == 'l':
    print(f"You are {0.4535924*int(weight)} kilos")
elif unit.lower() == 'k':
    print(f"you are {int(weight)/0.4535924} pounds")
else:
    print("Please enter the right unit")