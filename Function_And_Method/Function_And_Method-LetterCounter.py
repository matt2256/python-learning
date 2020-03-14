def up_low(s):
    upperCount = 0
    lowerCount = 0

    for char in s:
        if char.isupper():
            upperCount += 1
        elif char.islower():
            lowerCount += 1
    print("Upper: " + str(upperCount))
    print("Lower: " + str(lowerCount))


up_low("This Is A Good Day")
