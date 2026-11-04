import pandas

def main():
    data = pandas.read_csv('nato_phonetic_alphabet.csv')
    letters_dict = {row.letter:row.code for (_, row) in data.iterrows()}
    user_input = input('Enter a word: ').strip().upper()
    input_code = [letters_dict[letter] for letter in user_input]
    print(input_code)


if __name__ == "__main__":
    main()

