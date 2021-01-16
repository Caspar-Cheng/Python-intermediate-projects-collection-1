import pandas

# dictionary needs to be pandas.DataFrame(dict) before using iterrows(); 
# here is already a DataFrame format after the pandas.read_csv() method
alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")

letter_dict = {row.letter : row.code for (index, row) in alphabet_data.iterrows()}

word = input("Enter a word: ").upper()
output_list = [letter_dict[letter] for letter in word]

print(output_list)
