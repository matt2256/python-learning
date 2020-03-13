# Det virker med 3 tal
def has_33(nums):
    numList = list(map(int, str(nums)))

    if numList[0] == numList[1]:
        return True
    elif (numList[1] == numList[0]) or (numList[1] == numList[2]):
        return True
    elif numList[2] == numList[1]:
        return True
    else:
        return False


print(has_33(333))


def has_rnd_nums(num):
    for i in range(0, len(num) - 1):
        if num[i] == 3 and num[i + 1] == 3:
            return True
    return False


print(has_rnd_nums([1, 3, 1, 3]))
