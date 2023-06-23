
def capitalize_words(sentence):
    # Split the sentence into a list of words
    words = sentence.split()

    # Capitalize the first letter of each word
    capitalized_words = [word.capitalize() for word in words]

    # Join the capitalized words back into a string
    capitalized_sentence = " ".join(capitalized_words)

    # Return the new capitalized sentence
    return capitalized_sentence

input_sentence = capitalize_words(input("Please enter your sentence: "))
print(input_sentence)
