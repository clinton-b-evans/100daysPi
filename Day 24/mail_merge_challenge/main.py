# OPEN STARTING LETTER TEMPLATE 
with open("Input/Letters/starting_letter.txt") as file:
    contents = file.read()
    letter_template = contents

# CREATE LIST FROM INVITED NAMES
with open("Input/Names/invited_names.txt") as file:
    content = file.read()
    invited_names = content.splitlines()

# RUN LOOP FOR EACH NAME IN LIST AND CREATE INDIVIDUAL LETTER
for name in invited_names:
    new_letter = letter_template.replace("[name]", name)
    with open(f"Output/ReadyToSend/{name}_invite.txt",mode="w") as file:
        file.write(new_letter)

