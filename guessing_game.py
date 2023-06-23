secret_number = 7
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("enter your guess: "))
    guess_count += 1
    if guess == secret_number:
        print("Congratulations, You made the right guess")
        break
else:
     print("Sorry, you failed")