'''The transformation can be represented by aligning two alphabets; the cipher alphabet is the plain alphabet rotated left or right by some number of positions.

For instance, here is a Caesar cipher using a left rotation of three places, equivalent to a right shift of 23 (the shift parameter is used as the key):

Plain:  ABCDEFGHIJKLMNOPQRSTUVWXYZ

Cipher: XYZABCDEFGHIJKLMNOPQRSTUVW

When encrypting, a person looks up each letter of the message in the “plain” line and writes down the corresponding letter in the “cipher” line.

Plaintext:  THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG

Ciphertext: QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD

Deciphering is done in reverse, with a right shift of 3.'''

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

input_text = input("please input your message: ").upper()
key = int(input("Please enter the key: "))

cipher_text = ""
for text in input_text:
    if text in alphabets:
        text_index = alphabets.find(text)
        new_text_index = (text_index - key) %26
        cipher_text += alphabets[new_text_index]
    else:
        cipher_text += text
print(cipher_text)



