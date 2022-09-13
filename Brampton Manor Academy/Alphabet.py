alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
letter = input("Enter a letter from the alphabet")
found = False
count = 0

def position(letter):
    if alphabet[0] == letter.lower():
        suffix = "st"
        return suffix
    elif alphabet[1] == letter.lower():
        suffix = "nd"
        return suffix
    elif alphabet[2] == letter.lower():
        suffix = "rd"
        return suffix
    else:
        suffix = "th"
        return suffix

while found == False:
    if alphabet[count] == letter.lower():
        print(f"{letter} is {count+1}{position(letter)} in the alphabet")
        found = True
    else:
        count = count + 1
        

    


