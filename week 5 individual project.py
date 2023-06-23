#input
principal = float(input("please input the principal amount: GHS"))
interest = float(input("please enter the interest rate(as percentage): "))
year = float(input("enter number of years: "))

#convert
# M = P [ i(1 + i)^n ] / [ (1 + i)^n – 1]
#M = Total monthly payment
#P = The total amount of your loan
#i = Your interest rate, as a monthly percentage
#N = The total amount of months in your timeline for paying off your mortgage.
#convert interest
i = (interest / 100) / 12
N = year * 12
#calculate m(total monthly payment)
Total_monthly_payment = principal * (i * (1 + i) ** N) / ((1 + i) ** N - 1)

Total_amount_paid = Total_monthly_payment * N

print(f" \033[1m Result ... \033[0m \nFor a {year}-year mortgage loan of GHS{principal} \
at an annual interest rate of {interest} % you pay")
print(f" \033[1m{round(Total_monthly_payment, 2)} monthly \033[0m")
print("----------------------------")
print(f" \033[1m Total amount paid \033[0m {round(Total_amount_paid, 2)}")
print("----------------------------")