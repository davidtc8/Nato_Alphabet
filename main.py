# Creating our Nato Alphabet Code
import pandas as pd
df = pd.read_csv(r"nato_phonetic_alphabet.csv")

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

nato_dict = {row.letter:row.code for (index, row) in df.iterrows()}

name = input("Enter your name: ")
words_in_name = [letter.title() for letter in name]
nato_alphabet = [row for word in words_in_name for (index, row) in nato_dict.items() if word in row]

# Long way
#for word in words_in_name:
#    for (index, row) in nato_dict.items():
#        if word in row:
#            print(row)

print(nato_alphabet)
