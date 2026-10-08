PLACEHOLDER = "[name]"

def main():
    with open("Input/Letters/starting_letter.txt", mode="r") as data:
        letter = data.read()

    with open("Input/Names/invited_names.txt", mode="r") as data:
        names = data.readlines()

    for name in names:
        stripped_name = name.strip()
        new_letter = letter.replace(PLACEHOLDER, f"{stripped_name}")
        with open(f"Output/ReadyToSend/{stripped_name}.txt", mode="w") as data:
            data.write(new_letter)


if __name__ == "__main__":
    main()