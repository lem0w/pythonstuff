import string #Python module for strings. It contains a collection of string constants
import random #Python's module for generating random objects
lowercase_letters = string.ascii_lowercase #A constant containing lowercase letters
uppercase_letters = string.ascii_uppercase #A constant containing uppercase letters
def uppercase_word(): #The function responsible for generating #random words which are in uppercase
    word = '' #The variable which will hold the random word
    random_word_length = random.randint(1,10) #The random length of the word
    while len(word) != random_word_length: #While loop
        word += random.choice(uppercase_letters)
    return word
print(lowercase_word('m','b'))