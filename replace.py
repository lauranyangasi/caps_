# declaring the variable
string = "Laura is a happy girl"
# declaring variable to store our output
str_modified = ''
# setting conditions
for char in range(0, len(string)):
    if(string[char] == 'a' or string[char] == 'a'.upper()):
        str_modified += '$'
    else:
        str_modified += string[char]

print("modified string : ")
print(str_modified)


