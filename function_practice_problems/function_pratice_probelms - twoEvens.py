#lesser than two evens 

def twoEvens(a,b):
    # both number are even
    if a%2 == 0 and b%2==0:
        #both numbers are even
        if a < b:
            result = print(a)
        else: 
            result = print(b)
    else:
        #one or both number are odd
        if a > b:
            result = print(a)
        else:
            result = print(b)
    return result


twoEvens(2,5)




