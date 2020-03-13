print("This is a sentence.".startswith("T"))


def animal_craker(text):
    wordlist = text.split()
    firstLetter = wordlist[0]
    secoundLetter = wordlist[1]
    #Checks if both letters starts with the same letter 
    if firstLetter[0] == secoundLetter[0] and secoundLetter[0] == firstLetter[0]:
        return True
    else: 
        return False

    

print(animal_craker("Levelheaded Clama"))

