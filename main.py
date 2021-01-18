counts = [1,2,3,4,5,6,7,8]
name = []
replaced = []
with open("Input/Names/invited_names.txt") as data:
    for line in data:
        name.append(line)
    for eachname in name:
        names = eachname.strip("\n")
        name[name.index(eachname)] = names
with open("Input/Letters/starting_letter.docx") as mail:
    content = mail.read()
for count in counts:
    for names in name:
        replaced.append(content.replace("[name]", f"{names}"))
for count in counts:
    for rep in replaced:
        with open(f"Output/ReadyToSend/{count}.txt", "w") as final:
                final.write(rep)
