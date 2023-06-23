
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

input_text = input("please input your message: ").upper()
key = int(input("Please enter the key: "))

cipher_text = ""
for text in input_text:
    if text in alphabets:
        text_index = alphabets.find(text)
        new_text_index = (text_index + key) %26
        cipher_text += alphabets[new_text_index]
    else:
        cipher_text += text
print(cipher_text)