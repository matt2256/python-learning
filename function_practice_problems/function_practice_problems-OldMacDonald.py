def old_macdonald(name):
    firstLetter = name[0].upper()
    fourthLetter = name[3].upper()

    newname = "".join([firstLetter, name[1:3], fourthLetter, name[4::]])
    return newname


print(old_macdonald("mikkel"))


