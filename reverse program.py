def reverse_string(input_string):
    # Use slice notation to reverse the string
    reversed_string = input_string[::-1]

    # Return the reversed string
    return reversed_string



input_string = reverse_string(input("please enter your text: "))
print(input_string)