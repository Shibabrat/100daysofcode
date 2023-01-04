# Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".


PATH_TO_TEMPLATE = "./Input/Letters/"
TEMPLATE_FILENAME = "starting_letter.txt"

PATH_TO_NAMES = "./Input/Names/"
INVITEES_FILENAME = "invited_names.txt"

PATH_TO_LETTERS = "./Output/ReadyToSend/"

with open(PATH_TO_NAMES + INVITEES_FILENAME) as file1:
    friends_to_invite = file1.readlines()

for friends in friends_to_invite:
    with open(PATH_TO_TEMPLATE + TEMPLATE_FILENAME) as file:
        line = file.readlines()

    line[0] = str(line[0]).replace("[name]", friends.strip("\n"))
    line[6] = str(line[6]).replace("Angela", "Shibabrat")
    # print(line)

    LETTER_FILENAME = "letter_for_" + str(friends.strip("\n")) + ".txt"
    with open(PATH_TO_LETTERS + LETTER_FILENAME, "w") as file:
        file.writelines(line)
