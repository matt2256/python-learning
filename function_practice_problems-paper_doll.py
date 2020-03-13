def paper_dol(text):
    result = ""

    for char in text:
        result += char*3
    return result


print(paper_dol("Hello"))
