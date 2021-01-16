import pandas

alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")

letter_dict = {row.letter : row.code for (index, row) in alphabet_data.iterrows()}

word = input("Enter a word: ").upper()
output_list = [letter_dict[letter] for letter in word]

print(output_list)
