weight = int(input("Weight: "))
unit = input("(L)bs or (K)g: ")
if unit.upper() == "L":
    new_weight = weight * 0.45
    print(f"Your weight is {new_weight} kilos")
else:
    new_weight = weight / 0.45
    print(f"Your weight is {new_weight} lbs")

