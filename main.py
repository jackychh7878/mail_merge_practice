#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("./input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()

with open("./input/Names/invited_names.txt") as name_file:
    names = name_file.read().split("\n")

for each_name in names:
    new_letter = letter.replace("[name]", each_name)
    with open (f"./Output/ReadyToSend/{each_name}.txt", "w") as new_letter_file:
        new_letter_file.write(new_letter)
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp