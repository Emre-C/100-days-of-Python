#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
with open("./Input/Names/invited_names.txt", "r") as invited_names:
    names = invited_names.readlines()

for name in names:
    with open("./Input/Letters/starting_letter.txt", "r") as starting_letter:
        new_letter = starting_letter.read()
        new_letter = new_letter.replace("[name]", name.strip())
        with open(f"./Output/ReadyToSend/{name.strip()}.txt", "w") as output:
            output.write(new_letter)


#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp