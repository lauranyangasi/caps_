#input fuction
principal = float(input("mortage loan principal: GHS "))
interest_rate = float(input("percent annual interest (as a percentage): "))
years = int(input("years to pay off mortage (in years): "))

#we first convert the interest rate to a monthly percentage
#also convert the years to the total number of months to pay the mortgage

monthly_interest_rate = (interest_rate /100) / 12
monthly_term = (years * 12)

#calculate the total monthy payment
Total_monthly_payment = principal[monthly_interest_rate(1 + monthly_interest_rate)^monthly_term] / [(1 + monthly_interest_rate) ^ monthly_term - 1]
#calculate total amount paid
total_amount = Total_monthly_payment * 12


#print results
print(f"The {years}-year mortage loan of GHS{principal:.2f} at an annual intererst rate of {interest_rate:.2f}%, you pay")
print("your montly pay is: GHS", )
print("total amount paid is: GHS", )