# Creating our Nato Alphabet Code
import pandas as pd
import time
df = pd.read_csv(r"nato_phonetic_alphabet.csv")

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

nato_dict = {row.letter:row.code for (index, row) in df.iterrows()}

name = input("Enter your name: ").upper()
try:
    nato_alphabet = [nato_dict[letter] for letter in name]
    #words_in_name = [letter.title() for letter in name]
    #nato_alphabet = [row for word in words_in_name for (index, row) in nato_dict.items() if word in row]
    print(nato_alphabet)
except KeyError:
    print("Sorry, only letters in the alphabet Unu")

# Long way
#for word in words_in_name:
#    for (index, row) in nato_dict.items():
#        if word in row:
#            print(row)
