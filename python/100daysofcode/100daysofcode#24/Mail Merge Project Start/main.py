PLACEHOLDER="[name]"

with open("./Input/Names/invited_names.txt") as names:
    names_list=names.readlines()
    print(names_list)

with open('./Input/Letters/starting_letter.txt')as letter:
    letter_content=letter.read()
    for names in names_list:
        names=names.strip()
        letter_new=letter_content.replace(PLACEHOLDER,names)
        with open(f"./Output/ReadyToSend/letter_for_{names}.txt", mode="w") as completed_letter:
            completed_letter.write(letter_new)
            