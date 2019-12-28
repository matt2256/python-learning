def myfunc(*args):
    even_numbers = []
    for x in args:
        if isinstance(x, int):
            if x % 2 == 0:
                even_numbers.append(x)
    return even_numbers
            

print(myfunc(5,6,7,8))
    


