def master_yoda(text):
    newText = text.split()
    reverseText = "".join([newText[2], " ", newText[1], " ",newText[0]])
    return reverseText


print(master_yoda("hello new world"))