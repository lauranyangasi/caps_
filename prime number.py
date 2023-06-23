prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
my_number = int(input("please enter a number: "))

if my_number in prime_numbers:
    print("The list contains the mumber", my_number)
else:
    print("The list does not contain the number", my_number)

print(prime_numbers[0])
