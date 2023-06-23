charge_of_food = float(input("please enter the charge of the food: "))
# calculate 18%tip and 7%sales tax
tip = 0.18 * charge_of_food
sales_tax = 0.07 * charge_of_food

# add everything and display charge, tip and tax
total_charge = charge_of_food + tip + sales_tax

# print
print(f"your tip for the food is ${tip: .2f}")
print(f"sales tax the food is ${sales_tax: .2f}")
print(f"your total charge for the food is ${total_charge:.2f}")
