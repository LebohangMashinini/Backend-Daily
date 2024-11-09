def letter_file():
    try:
        with open("./Input/letters/starting_letter.docx", "r") as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        print("error: starting_letter.docx file not found")
        return []
def names_file():
    names = []
    try:
        f = open('./Input/Names/inivited_names.txt', 'r')
        contents = f.readlines()
        for line in contents:    
            names.append(line.strip())
        return names
    except FileNotFoundError:
        print("Error: inivited_names.txt file not found")
        return []

def construct_letter():
    names =  names_file()
    if not names:
        print("No names found. Aborting")

    letter_content = letter_file()
    if not letter_content:
        print("No letter content found. Aborting")

    letter = "".join(letter_content)
    new_letter = ''

    for name in names:
        new_letter = letter.replace("[name]",name)
        try:
            with open(f"./Input/ReadyToSend/{name}.docx", "w") as file:
                file.write(new_letter)
        except IOError:
            print("Error: could not create a letter")
            

if __name__ == "__main__":
    construct_letter()
#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp